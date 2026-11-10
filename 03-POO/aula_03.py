class Carro:
    def __init__(self,nome):
        self.nome = nome

    def acelerar(self):
        print(self.nome, ' está a acelerar')


carro_0=Carro('porshe')

print(carro_0.nome)
carro_0.acelerar()


carro_1= Carro('BMW')
print(carro_1.nome)
carro_1.acelerar()
print()
print('.........................')
print('OUTRA HISTÓRIA')
print('.........................')
print(Carro.acelerar(carro_0))