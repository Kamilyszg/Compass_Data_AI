lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def f(x):
    return x ** 2

def my_map(lista, f):
    lista2 = map(f, lista)
    return lista2

print(list(my_map(lista, f)))