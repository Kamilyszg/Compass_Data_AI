def removerDuplicatas(lista):
    numeros_unicos = set(lista)
    nova_lista = list(numeros_unicos)
    print(nova_lista)

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

removerDuplicatas(lista)