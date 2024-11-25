def dividir(lista):
    lista1 = []
    lista2 = []
    lista3 = []
    numero = len(lista) // 3
    for i in range(numero):
        lista1.append(lista[i])
        lista2.append(lista[i+4])
        lista3.append(lista[i+8])
    return f"{lista1} {lista2} {lista3}"
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(dividir(lista))