import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import *
import pyspark.sql.functions as func

## @params: [JOB_NAME, S3_INPUT_PATH, S3_OUTPUT_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Definindo o esquema para os dados JSON
arqschema = StructType([
    StructField("id", IntegerType(), True),
    StructField("imdb_id", StringType(), True),
    StructField("title", StringType(), True),
    StructField("original_title", StringType(), True),
    StructField("genre_ids", ArrayType(IntegerType()), True),
    StructField("genres", StringType(), True),
    StructField("popularity", FloatType(), True),
    StructField("release_date", DateType(), True),
    StructField("vote_average", FloatType(), True),
    StructField("vote_count", IntegerType(), True),
    StructField("production_countries", StringType(), True),
    StructField("production_companies", StringType(), True),
    StructField("budget", FloatType(), True),
    StructField("revenue", FloatType(), True),
    StructField("status", StringType(), True),
    StructField("most_popular_actor", StringType(), True),
    StructField("actor_popularity", FloatType(), True),
    StructField("ator_nacionalidade", StringType(), True),
    StructField("director", StringType(), True),
    StructField("director_popularity", FloatType(), True),
])

# Lendo os arquivos JSON do S3 para um DynamicFrame
movies_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="json",
    format_options={"multiline": True}
)

# Convertendo para um DataFrame do Spark
spark_df = movies_df.toDF()

# Realizando transformações no DataFrame
df_limpo = spark_df.dropna(subset=["imdb_id"])  # Remover filmes sem imdb_id
df_limpo = df_limpo.fillna("desconhecido", subset=["most_popular_actor", "ator_nacionalidade", "director"])  # Preencher valores nulos
df_limpo = df_limpo.withColumnRenamed("ator_nacionalidade", "actor_nationality")  # Renomear coluna

# Convertendo de volta para um DynamicFrame
dynamic_df = DynamicFrame.fromDF(df_limpo, glueContext, "dynamic_df")

# Salvando o resultado final em formato Parquet no S3
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_df,
    connection_type="s3",
    connection_options={"path": target_path},
    format="parquet"
)

job.commit()