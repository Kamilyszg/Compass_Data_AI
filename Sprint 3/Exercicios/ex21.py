class Passaro:
    def voar(self):
        print('voando')
    
    def emitir_som(self):
        pass

class Pato(Passaro):
    def voar(self):
        print('Pato')
        super().voar()
        
    def emitir_som(self):
        print('Quack Quack')

class Pardal(Passaro):
    def voar(self):
        print('Pardal')
        super().voar()
        
    def emitir_som(self):
        print('Piu Piu')


passaro = Passaro()

pato = Pato()
pato.voar() 
pato.emitir_som()

pardal= Pardal()
pardal.voar()
pardal.emitir_som()