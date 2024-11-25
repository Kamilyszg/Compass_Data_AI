class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
    
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
        
    def esta_ligada(self):
        return self.ligada

l1 = Lampada(False)

Lampada.liga(l1)
print(Lampada.esta_ligada(l1))
Lampada.desliga(l1)
print(Lampada.esta_ligada(l1))