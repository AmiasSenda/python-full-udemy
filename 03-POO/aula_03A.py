class Carro:
    def __init__(self,nome):
        self.nome = nome
    def acelerar (self):
        print(self.nome,' Está a acelerar')


carro_1 = Carro('porshe')

Carro.acelerar(carro_1)