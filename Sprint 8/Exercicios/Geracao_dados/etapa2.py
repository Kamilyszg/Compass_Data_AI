import csv

animais = ["Baleia", "Canguru", "Borboleta", "Peixe", "Mosca", 
            "Grilo", "Cachorro", "Gato", "Papagaio", "Rato",
            "Arara", "Sapo", "Porco", "Camelo", "Crocodilo",
            "Urso", "Gorila", "Macaco", "Cabra", "Ovelha"]

def transformar_csv(animais):
    with open('animais.csv', mode='w', newline='') as file:
        escrita = csv.writer(file)
        escrita.writerows([[animal] for animal in animais])

def ordenacao_alfabetica(animais):
    animais = [animal for animal in sorted(animais)]
    print(animais)
    transformar_csv(animais)

def main():
    ordenacao_alfabetica(animais)

main()