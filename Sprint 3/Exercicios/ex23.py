class  Calculo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def soma(self):
        print('Somando:')
        resultado = self.x + self.y
        print(f'{self.x}+{self.y} = {resultado}')
        
    def subtrai(self):
        print('Subtraindo:')
        resultado = self.x - self.y
        print(f'{self.x}-{self.y} = {resultado}')
         
        
s = Calculo(4,5)

s.soma()
s.subtrai()