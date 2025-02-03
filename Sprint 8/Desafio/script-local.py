# Passo a passo:

# 1. Conexao com o bucket s3

# 2. Acesso ao caminho s3://data-lake-kamily/Raw/Local/CSV/Movies/2025/01/03/movies.csv

# 3. Manipulação do arquivo CSV: Limpeza dos dados

# 4. Conversão para formato Parquet

# 5. Envio para o caminho s3://bucket/Trusted/Local/Parquet/movies/movies.parquet

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

movies_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)
spark_df = movies_df.toDF()  # Converter DynamicFrame para Spark DataFrame

spark_df = spark_df.dropDuplicates()

dynamic_df = DynamicFrame.fromDF(spark_df, glueContext, "dynamic_df")

glueContext.write_dynamic_frame.from_options(
    frame=dynamic_df,
    connection_type="s3",
    connection_options={"path": target_path},
    format="parquet"
)

job.commit()
