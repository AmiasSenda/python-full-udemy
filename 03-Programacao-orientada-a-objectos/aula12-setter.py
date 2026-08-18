class Caneta:
    def __init__(self,cor):
        self.cor_tinta =  cor
        #PRIVATE PROTECTED
        self._cor = cor


    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

    def mostrar(caneta):
        return caneta.cor

caneta = Caneta('Pink')


caneta.cor = 'Blue'

print(caneta.cor)
    
        