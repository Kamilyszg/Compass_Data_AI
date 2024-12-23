import boto3
import pandas as pd

client = boto3.client('s3', 
    aws_access_key_id = '',
    aws_secret_access_key = '',
    aws_session_token = '')


client.download_file(Bucket='desafio-sp5-kamily', Key ='csv_original', Filename='arquivo_original.csv')

with open('arquivo_original.csv', 'r', encoding='latin-1') as file: 
    #leitura do arquivo
    dados_df = pd.read_csv(file, delimiter=';')

#Tratamento dos dados
#Verificação de duplicatas - Foram encontradas 2 linhas
duplicatas = dados_df[dados_df.duplicated(keep=False)]
#print(duplicatas)

#Remoção das duplicatas
dados_df = dados_df.drop_duplicates(keep='first')
#print(dados_df.duplicated().sum())

""" Verificação dos tipos dos dados presentes em cada coluna e a presença de dados nulos
dados_df.shape
dados_df.info()
"""
#Preenchimento dos espaços nulos
dados_df['SigAgenteAcessante'] = dados_df['SigAgenteAcessante'].fillna('Não se aplica')
#dados_df.info()

#Renomeação das colunas para melhor leitura
dados_df = dados_df.rename(columns={'DscREH': 'Resoluçao_Homologatoria', 'SigAgente': 'Agente', 'DatInicioVigencia':'Inicio_Vigencia', 'DatFimVigencia': 'Fim_Vigencia', 'DscBaseTarifaria' : 'Base_Tarifaria', 'DscSubGrupo' : 'SubGrupo', 'DscModalidadeTarifaria':'Modalidade_Tarifaria', 'NomPostoTarifario': 'Posto_Tarifario', 'DscUnidadeTerciaria': 'Unidade', 'VlrTUSD': 'Valor_TUSD'})
#dados_df.info()

#Filtragem dos dados que possivemente serão utilizados na fase de analise - exclusão de colunas
dados_analise_df = dados_df[['Resoluçao_Homologatoria', 'Agente', 'Inicio_Vigencia', 'Fim_Vigencia', 'Base_Tarifaria', 'SubGrupo', 'Modalidade_Tarifaria', 'Posto_Tarifario', 'Unidade', 'Valor_TUSD']]

#Tornando o novo dataset em um arquivo
dados_analise_df.to_csv('arquivo_tratado.csv', index=False, sep=';')

#Envio do arquivo tratado para o bucket S3
client.upload_file(Filename='arquivo_tratado.csv', Bucket='desafio-sp5-kamily', Key='csv_tratado')