class Caneta:
    def __init__(self,cor):
        self.corTinta = cor
    @property
    def cor_tinta(self):
        print('PROPERTY')
        return self.corTinta

caneta = Caneta ('Azul')


print(caneta.corTinta)