import boto3
import pandas as pd

client = boto3.client('s3', 
    aws_access_key_id = '',
    aws_secret_access_key = '',
    aws_session_token = '')


client.download_file(Bucket='desafio-sp5-kamily', Key ='csv_tratado', Filename='arquivo_tratado.csv')

with open('arquivo_tratado.csv', 'r', encoding='utf-8-sig') as file: 
    #leitura do arquivo
    dados_analise_df = pd.read_csv(file, delimiter=';')

# Quais foram os anos em que os agentes CPFL - PAULISTA ou ERO apresentaram médias de tarifas acima da média geral anual para casos medidos em kW, analisando também a variabilidade dos valores?

#conversao
dados_analise_df['Valor_TUSD'] = dados_analise_df['Valor_TUSD'].str.replace(',', '.').astype(float)
#dados_analise_df.info()

#filtragem
dados_filtrados_df = dados_analise_df[(dados_analise_df['Base_Tarifaria'] == 'Tarifa de Aplicação') & (dados_analise_df['Unidade'] == 'kW') & ((dados_analise_df['Agente'] == 'CPFL-PAULISTA') | (dados_analise_df['Agente'] == 'ERO'))]

#data
dados_filtrados_df['Ano'] = pd.to_datetime(dados_filtrados_df['Inicio_Vigencia']).dt.year

#string
dados_filtrados_df['Agente'] = dados_filtrados_df['Agente'].str.title()
#print(dados_filtrados_df)

#agregacao
media_por_ano_agente = dados_filtrados_df.groupby(['Ano', 'Agente'])['Valor_TUSD'].mean().reset_index()
media_por_ano_agente.rename(columns={'Valor_TUSD': 'Media_Tarifaria'}, inplace=True)

desvio_padrao_por_ano_agente = dados_filtrados_df.groupby(['Ano', 'Agente'])['Valor_TUSD'].std().reset_index()
desvio_padrao_por_ano_agente.rename(columns={'Valor_TUSD': 'Desvio_Padrao'}, inplace=True)

estatisticas_anuais = pd.merge(media_por_ano_agente, desvio_padrao_por_ano_agente, on=['Ano', 'Agente'])
#print(estatisticas_anuais)

media_geral = estatisticas_anuais['Media_Tarifaria'].mean()
#print(media_geral)

#condicao
estatisticas_anuais['Acima_da_Media'] = estatisticas_anuais['Media_Tarifaria'].apply(lambda x: 'Sim' if x > media_geral else 'Não')
#(print(estatisticas_anuais))

resultados_acima_da_media = estatisticas_anuais[estatisticas_anuais['Acima_da_Media'] == 'Sim']
#print(resultados_acima_da_media)

#Tornando o novo resultado da análise em um arquivo
resultados_acima_da_media.to_csv('resultado_analise.csv', index=False, sep=';')

#Envio para o bucket S3
client.upload_file(Filename='resultado_analise.csv', Bucket='desafio-sp5-kamily', Key='csv_resultado')