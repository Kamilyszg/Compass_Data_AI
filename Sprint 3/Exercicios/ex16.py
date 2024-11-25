def soma (frase):
    numeros = list(map(int, frase.split(",")))
    soma = 0
    for i in range (len(numeros)):
        soma += numeros[i]
    return soma

frase = "1, 3, 4, 6, 10, 76"
print(soma(frase))