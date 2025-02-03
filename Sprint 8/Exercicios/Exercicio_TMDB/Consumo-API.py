import requests
import pandas as pd
from IPython.display import display

api_key = ""
url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
response = requests.get(url)
data = response.json()

generos = []

for genero in data['genres']:
    df = {'id': genero['id'], 'nome': genero['name']}
    generos.append(df)

df = pd.DataFrame(generos)
display(df)