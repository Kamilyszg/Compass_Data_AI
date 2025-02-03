import random

def gerar_dados():
    numeros = []
    for i in range(250):
        numeros.append(random.randint(-1000,1000))
    numeros.reverse()
    print(numeros)

def main():
    gerar_dados()

main()