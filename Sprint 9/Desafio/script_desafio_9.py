import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

#bibliotecas necessárias
from pyspark.sql.functions import *
from pyspark.sql.types import *

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_CSV_PATH', 'INPUT_TMDB_PATH', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#leitura dos arquivos Parquet usando os parâmetros
df_csv = spark.read.parquet(args['INPUT_CSV_PATH'])
df_tmdb = spark.read.parquet(args['INPUT_TMDB_PATH'])

# Ajustes csv

#filtragem dos gêneros 
df_csv = df_csv.filter((df_csv.genero.like('%Comedy%'))&(df_csv.genero.like('%Animation%')))

#conversão da coluna anoLancamento para int
df_csv= df_csv.withColumn("anoLancamento", col("anoLancamento").cast("int"))
#filtragem do período
df_csv = df_csv.filter((df_csv.anoLancamento >= 2018) & (df_csv.anoLancamento <= 2022))

#seleção das colunas csv
df_csv = df_csv.withColumnRenamed("tituloPincipal", "tituloPrincipal")
df_csv = df_csv.select("id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "genero", "notaMedia", "numeroVotos")

#remoção de duplicatas considerando o id
df_csv = df_csv.dropDuplicates(["id"])

# Ajustes TMDB

#seleção das colunas TMDB
df_tmdb = df_tmdb.select("imdb_id", "title", "original_title", "release_date", "genres", "popularity", "vote_average", "vote_count", "production_countries", "production_companies", "most_popular_actor", "actor_popularity", "actor_nationality", "director", "director_popularity")

# selecionando apenas o ano
df_tmdb = df_tmdb.withColumn("release_date", year(to_date(col("release_date"), "yyyy-MM-dd")))
# tornando o valor do ano em inteiro
df_tmdb = df_tmdb.withColumn("release_date", col("release_date").cast(IntegerType()))

#junção
df_merged = df_tmdb.join(df_csv, df_tmdb.imdb_id == df_csv.id, "left")

#utilização do método fallback
df_merged = df_merged.withColumn("title", coalesce(df_tmdb['title'], df_csv['tituloPrincipal']))
df_merged = df_merged.withColumn("original_title", coalesce(df_tmdb['original_title'], df_csv['tituloOriginal']))
df_merged = df_merged.withColumn("release_date", coalesce(df_tmdb['release_date'], df_csv['anoLancamento']))
df_merged = df_merged.withColumn("genres", coalesce(df_tmdb['genres'], df_csv['genero']))
df_merged = df_merged.withColumn("vote_average", coalesce(df_tmdb['vote_average'], df_csv['notaMedia']))
df_merged = df_merged.withColumn("vote_count", coalesce(df_tmdb['vote_count'], df_csv['numeroVotos']))

#remoção das colunas do csv já utilizadas
df_merged = df_merged.drop("id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "genero", "notaMedia", "numeroVotos")

#explode das colunas production_countries e production_companies devido a multiplicidade de valores nas células
df_merged = df_merged.withColumn("production_countries", split(col("production_countries"), ", "))
df_merged = df_merged.withColumn("production_companies", split(col("production_companies"), ", "))
df_exploded = df_merged.withColumn("production_countries", explode(col("production_countries")))
df_exploded = df_exploded.withColumn("production_companies", explode(col("production_companies")))

df_exploded.createOrReplaceTempView("merged")

# Escrita das tabelas de dimensão e fato com base no OUTPUT_PATH
output_path = args['OUTPUT_PATH']

movie_dim = spark.sql("SELECT imdb_id, title, original_title, release_date, genres FROM merged GROUP BY imdb_id, title, original_title, release_date, genres")
movie_dim.createOrReplaceTempView("movie_dim")
movie_dim.write.parquet(f"{output_path}/movie_dim/")

director_dim = spark.sql("SELECT director, director_popularity FROM merged GROUP BY director, director_popularity")
director_dim = director_dim.withColumn("director_id", monotonically_increasing_id())
director_dim = director_dim.select("director_id", "director", "director_popularity")
director_dim.createOrReplaceTempView("director_dim")
director_dim.write.parquet(f"{output_path}/director_dim/")

most_popular_actor_dim = spark.sql("SELECT DISTINCT most_popular_actor, actor_popularity, actor_nationality FROM merged")
most_popular_actor_dim = most_popular_actor_dim.filter(most_popular_actor_dim.most_popular_actor != 'desconhecido')
most_popular_actor_dim = most_popular_actor_dim.withColumn("most_popular_actor_id", monotonically_increasing_id())
most_popular_actor_dim = most_popular_actor_dim.select("most_popular_actor_id", "most_popular_actor", "actor_popularity", "actor_nationality")
most_popular_actor_dim.createOrReplaceTempView("most_popular_actor_dim")
most_popular_actor_dim.write.parquet(f"{output_path}/most_popular_actor_dim/")

production_country_dim = spark.sql("SELECT DISTINCT production_countries FROM merged")
production_country_dim = production_country_dim.withColumn("production_country_id", monotonically_increasing_id())
production_country_dim = production_country_dim.select("production_country_id", "production_countries")
production_country_dim.createOrReplaceTempView("production_country_dim")
production_country_dim.write.parquet(f"{output_path}/production_country_dim/")

production_company_dim = spark.sql("SELECT DISTINCT production_companies FROM merged")
production_company_dim = production_company_dim.withColumn("production_company_id", monotonically_increasing_id())
production_company_dim = production_company_dim.select("production_company_id", "production_companies")
production_company_dim = production_company_dim.withColumn(
    "production_companies",when(production_company_dim["production_companies"] == "", "desconhecido")
    .otherwise(production_company_dim["production_companies"])
)
production_company_dim.createOrReplaceTempView("production_company_dim")
production_company_dim.write.parquet(f"{output_path}/production_company_dim/")

# Tabela Fato
spark.sql("""
    SELECT DISTINCT m.imdb_id, m.popularity, m.vote_average, m.vote_count, 
                    mpad.most_popular_actor_id, dd.director_id
    FROM merged m
    INNER JOIN most_popular_actor_dim mpad ON m.most_popular_actor = mpad.most_popular_actor
    INNER JOIN director_dim dd ON m.director = dd.director
""").write.parquet(f"{output_path}/fact_movie/")

# Tabelas bridge
bridge_country_fact = spark.sql(""" 
    SELECT
        m.imdb_id, 
        pc.production_country_id
    FROM 
        production_country_dim pc
    JOIN 
        merged m 
        ON pc.production_countries = m.production_countries
    GROUP BY 
        m.imdb_id, 
        pc.production_country_id;
""")
bridge_country_fact.write.parquet(f"{output_path}/bridge_country_fact/")

bridge_company_fact = spark.sql("""
    SELECT
        m.imdb_id,
        pcom.production_company_id
    FROM
        production_company_dim pcom
    JOIN
        merged m
        ON pcom.production_companies = m.production_companies
    GROUP BY
        m.imdb_id,
        pcom.production_company_id
""")
bridge_company_fact.write.parquet(f"{output_path}/bridge_company_fact/")

# Finalização do job
job.commit()