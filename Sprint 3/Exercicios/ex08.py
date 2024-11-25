lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

palindromo = False
for palavra in lista:
    tamanho = len(palavra)
    for i in range(tamanho // 2): #quantas vezes irá rodar dentro da palavra - até a metade
        if palavra[i] != palavra[tamanho - 1 - i]: 
            palindromo = False 
            print(f'A palavra: {palavra} não é um palíndromo')
            break
    else:
        palindromo = True
        print(f'A palavra: {palavra} é um palíndromo')