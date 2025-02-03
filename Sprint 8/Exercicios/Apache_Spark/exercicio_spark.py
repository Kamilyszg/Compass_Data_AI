# -*- coding: utf-8 -*-
"""
# Etapa 1 - Preparação do ambiente

Importação das bibliotecas
"""

from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

"""Inicialização da sessão"""

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

"""leitura do arquivo e transformação em DataFrame"""

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, sep="\n")
df_nomes.show(5)

"""# Etapa 2 - Renomeação da coluna"""

df_nomes.printSchema()

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.show(10)

"""# Etapa 3 - Adição da coluna Escolaridade"""

from pyspark.sql import functions as f

niveis = ["Fundamental", "Médio", "Superior"]

df_nomes = df_nomes.withColumn("Escolaridade", f.when(f.rand()<0.33, niveis[0]).when(f.rand()<0.66, niveis[1]).otherwise(niveis[2]))
df_nomes.show()

"""# Etapa 4 - Adição da coluna país"""

paises = [ "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia",
    "Equador", "Guiana Francesa", "Paraguai", "Peru", "Suriname",
    "Uruguai", "Venezuela", "Guiana"]

df_nomes = df_nomes.withColumn(
    "País",
    f.when(f.rand() < 1/13, paises[0])
    .when(f.rand() < 2/13, paises[1])
    .when(f.rand() < 3/13, paises[2])
    .when(f.rand() < 4/13, paises[3])
    .when(f.rand() < 5/13, paises[4])
    .when(f.rand() < 6/13, paises[5])
    .when(f.rand() < 7/13, paises[6])
    .when(f.rand() < 8/13, paises[7])
    .when(f.rand() < 9/13, paises[8])
    .when(f.rand() < 10/13, paises[9])
    .when(f.rand() < 11/13, paises[10])
    .when(f.rand() < 12/13, paises[11])
    .otherwise(paises[12])
)

df_nomes.show()

"""# Etapa 5 - Adição da coluna AnoNascimento"""

df_nomes = df_nomes.withColumn("AnoNascimento", (f.rand() * (2011 - 1945) + 1945).cast("int"))
df_nomes.show()

#df_nomes.groupBy("AnoNascimento").count().orderBy("AnoNascimento").show(df_nomes.count(), truncate=False)

"""# Etapa 6 - Selecionar os nomes do século atual"""

df_select = df_nomes.select("*").where("AnoNascimento >= 2001")
df_select.show(10)

"""# Etapa 7 - Repetir o passo anterior em tabelas temporárias"""

df_nomes.createOrReplaceTempView("pessoas")
spark.sql("select * from pessoas").show()

spark.sql("create or replace temp view pessoas_select as select * from pessoas where AnoNascimento >= 2001")
spark.sql("select * from pessoas_select").show(10)

"""# Etapa 8 - Contar o número de pessoas Millenials (1980-1994) com filter()"""

contagem = df_nomes.filter((f.col("AnoNascimento")>=1980) & (f.col("AnoNascimento") <= 1994)).count()
print(contagem)

"""# Etapa 9 - Repetir o passo anterior utilizando Spark SQL"""

spark.sql("select count(*) from pessoas where AnoNascimento >= 1980 and AnoNascimento <= 1994").show()

"""# Etapa 10 - Usando Spark SQL obtenha a quantidade de pessoas de cada país para cada uma das gerações abaixo:

*   Baby Boomers: 1944 - 1964
*   Geração X: 1965 - 1979
*   Millennials (Geração Y): 1980 - 1994
*   Geração Z: 1995 - 2015

### Armazene o resultado em um novo DataFrame e mostre todas as linhas em ordem crescente de País, Geração e Quantidade."""

df_geracoes = spark.sql("""
    SELECT
        `País`,
        CASE
            WHEN anoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN anoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN anoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            WHEN anoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
        END AS `Geração`,
        COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY `País`, `Geração`
    ORDER BY `País`, `Geração`, Quantidade
""")
df_geracoes.show()

