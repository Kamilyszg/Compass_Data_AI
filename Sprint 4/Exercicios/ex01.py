with open('number.txt', 'r') as number:
    numeros = map(int, number)
    
    pares = filter(lambda x: x % 2 == 0, numeros)
    pares_ordenados = sorted(pares, reverse=True)
    cinco_maiores_pares = list(pares_ordenados[:5])
    soma = sum(cinco_maiores_pares)
    
print(cinco_maiores_pares)
print(soma)