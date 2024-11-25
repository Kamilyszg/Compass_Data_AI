class Aviao:
    
    cor='Azul'
    
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

        
    def __str__(self):
        return  f"O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima} km/h, capacidade para {self.capacidade} passageiros e é da cor {self.cor}."


a1 = Aviao('BOIENG456', 1500, 400)
a2 = Aviao('Embraer Praetor 600', 863, 14)
a3 = Aviao('Antonov An-2', 258, 12)


lista = [a1, a2, a3]

for aviao in lista:
    print(aviao)