class Carro:
#self - instância da própria class,em  outras palavras (Eu mesmo)
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print('o carro ',self.nome,' está acelerando')

carro_1  = Carro('Fusca')
print(carro_1.nome)
carro_1.acelerar()

outro_carro = Carro('Celta')
print(outro_carro.nome)
outro_carro.acelerar()