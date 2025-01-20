import requests
import json
import boto3
from datetime import datetime

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    api_key = ''

    #parametros do discover/movie
    params = {
        'api_key': api_key,
        'language': 'pt-BR',
        'primary_release_date.gte': '2020-01-01',
        'primary_release_date.lte': '2024-12-31',
        'with_genres': '35,16',
        'without_genres' : '28|12|80|99|18|10751|14|36|27|10402|9648|10749|878|10770|53|10752|37'
    }

    url = f"https://api.themoviedb.org/3/discover/movie"

    #verificado na consulta no próprio site
    total_pages = 27  #total de páginas de resultados

    movies = []

    columns = [
        'imdb_id', 
        'production_countries', 
        'production_companies', 
        'budget', 
        'revenue', 
        'status'
    ]

    # Loop para percorrer todas as páginas e pegar os filmes
    for page in range(1, total_pages + 1):
        params['page'] = page  # Atualiza o parâmetro de página para a página atual
        discover_response = requests.get(url, params=params)  # Faz a requisição para a API
        if discover_response.status_code == 200:
            data = discover_response.json()
        else:
            print(f"Erro ao acessar a página {page}: {discover_response.status_code}")
            continue

        for movie in data['results']:
            movies_dict = {
                'id': movie.get('id'),
                'title': movie.get('title'),
                'original_title': movie.get('original_title'),
                'genre_ids': movie.get('genre_ids'),
                'popularity': movie.get('popularity'),
                'release_date': movie.get('release_date'),
                'vote_average': movie.get('vote_average'),
                'vote_count': movie.get('vote_count')
            }

            details_url = f"https://api.themoviedb.org/3/movie/{movie['id']}"
            detail_params = {'api_key': api_key}
            id_external_response = requests.get(details_url, params=detail_params)

            if id_external_response.status_code == 200:
                details_data = id_external_response.json()

                for col in columns:
                    if col == 'production_countries':
                        countries = details_data.get('production_countries', [])
                        movies_dict[col] = ', '.join([country.get('name') for country in countries])
                    elif col == 'production_companies':
                        companies = details_data.get('production_companies', [])
                        movies_dict[col] = ', '.join([company.get('name') for company in companies])
                    else:
                        movies_dict[col] = details_data.get(col, None)

                #transformação do resultado em string
                genres = details_data.get('genres', [])
                movies_dict['genres'] = ', '.join([genre['name'] for genre in genres])
                
            else:
                print(f"Erro ao obter detalhes para o filme {movie['id']}: {id_external_response.status_code}")

            # requisição para obter atores e diretores
            credits_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits"
            credits_response = requests.get(credits_url, params=detail_params)

            if credits_response.status_code == 200:
                credits_data = credits_response.json()
                cast = credits_data.get('cast', [])
                crew = credits_data.get('crew', [])

                # Ordenar o elenco por popularidade e pegar o ator mais popular
                if cast:
                    most_popular_actor = max(cast, key=lambda x: x.get('popularity', 0))
                    movies_dict['most_popular_actor'] = most_popular_actor.get('name')
                    movies_dict['actor_popularity'] = most_popular_actor.get('popularity')
                else:
                    movies_dict['most_popular_actor'] = None
                    movies_dict['actor_popularity'] = None

                # Filtrar para encontrar o diretor
                director = next((person for person in crew if person.get('job') == 'Director'), None)
                movies_dict['director'] = director.get('name') if director else None
                movies_dict['director_popularity'] = director.get('popularity') if director else None
            else:
                print(f"Erro ao obter créditos para o filme {movie['id']}: {credits_response.status_code}")

                
            movies.append(movies_dict)

    data_atual = datetime.now()
    dia = data_atual.day
    mes = data_atual.month
    ano = data_atual.year

    fatia = []
    contador = 0

    bucket_name = 'data-lake-kamily'
    s3_path = f'Raw/TMDB/JSON/{ano}/{mes}/{dia}/'

    for registro in movies:
        fatia.append(registro)

        if len(fatia) == 100:
            contador+=1

            arquivo_json = json.dumps(fatia, ensure_ascii=False, indent=4)

            s3_key = f'{s3_path}arquivo_{contador}.json'
            s3_client.put_object(
                Bucket=bucket_name,
                Key=s3_key,
                Body=arquivo_json,
                ContentType='application/json'
            )
            
            fatia = []

    # Enviar os últimos registros restantes 
    if fatia:
        contador += 1
        arquivo_local = f"arquivo_{contador}.json"

        arquivo_json = json.dumps(fatia, ensure_ascii=False, indent=4)
        s3_key = f'{s3_path}arquivo_{contador}.json'
        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=arquivo_json,
            ContentType='application/json'
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Arquivos JSON enviados com sucesso!')
    }