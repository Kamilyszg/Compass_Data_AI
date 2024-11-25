import random

random_list = random.sample(range(500), 50)

random_list.sort()

n = len(random_list)

mediana = 0
if n % 2 == 0: #par
    mediana = (random_list[n // 2] + random_list[n // 2 - 1])/2
else:
    mediana = (random_list[n//2])

media = 0
media = sum(random_list) / n

valor_minimo = 0
valor_minimo = min(random_list)

valor_maximo = 0
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')