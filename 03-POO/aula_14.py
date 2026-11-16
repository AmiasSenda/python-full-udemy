#Property
class Caneta:
    def __init__(self, cor):
        #private #protected #public
        self.cor_tinta = cor
    @property
    def cor(self):
        return self.cor_tinta
    @property
    def cor_test(self):
        return 'corado'

caneta = Caneta ('Azul')
print(caneta.cor)
print(caneta.cor_test)


