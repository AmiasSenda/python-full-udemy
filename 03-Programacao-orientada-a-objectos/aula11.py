class Caneta:
    def __init__(self,cor):
        self.cor = cor
    def get_cor(self):
        return self.cor

caneta = Caneta ('Azul')


print(caneta.get_cor())