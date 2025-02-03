import names, os, time, random

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0,qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} números aleatórios".format(qtd_nomes_aleatorios))
dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open('nomes_aleatorios.txt', mode='w', newline='') as file:
    escrita = [file.write(nome + "\n") for nome in dados]

with open('nomes_aleatorios.txt', mode='r') as file2:
    conteudo = file2.read()
    print(conteudo)