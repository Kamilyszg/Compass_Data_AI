a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

lista_a = set(a)
lista_b = set(b)

lista_c = lista_a.intersection(lista_b)

print(list(lista_c))