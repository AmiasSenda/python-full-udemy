#Property
class Caneta:
    def __init__(self, cor):
        #private #protected #public
        self.cor_tinta = cor

    def get_cor(self):
        return self.cor_tinta

caneta = Caneta ('Azul')
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print()
