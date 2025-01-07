import boto3
from datetime import datetime

client = boto3.client('s3',
    aws_access_key_id='',
    aws_secret_access_key='',
    aws_session_token=''
    )

nome_bucket = 'data-lake-kamily'
client.create_bucket(Bucket= nome_bucket)

def upload_arquivos(filename):
    data_atual = datetime.today()
    categoria = filename.split(".")[0].capitalize()
    caminho_bucket = f'Raw/Local/CSV/{categoria}/{data_atual.year}/{data_atual.month:02}/{data_atual.day:02}/{filename}'
    caminho_local = f'/vol/{filename}'

    try:
        client.upload_file(caminho_local, nome_bucket, caminho_bucket)
        print(f"Upload do arquivo {filename} concluído.")
    except Exception as erro:
        print(f"Erro ao fazer upload: {erro}")


def main():
    upload_arquivos('movies.csv')
    upload_arquivos('series.csv')

main()


