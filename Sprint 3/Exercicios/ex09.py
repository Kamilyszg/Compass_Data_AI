# Você deve Utilizar a função enumerate().

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

juncao = zip(primeirosNomes, sobreNomes, idades)

for indice, (primeirosNomes, sobreNomes, idades) in enumerate(juncao):
    print(f'{indice} - {primeirosNomes} {sobreNomes} está com {idades} anos')