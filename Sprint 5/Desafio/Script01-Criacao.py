import boto3

client = boto3.client('s3', 
    aws_access_key_id = '',
    aws_secret_access_key = '',
    aws_session_token = '')

client.create_bucket(Bucket='desafio-sp5-kamily')

file_csv = './tarifas-homologadas-distribuidoras-energia-eletrica.csv'

client.upload_file(Filename= file_csv, Bucket='desafio-sp5-kamily', Key = 'csv_original')