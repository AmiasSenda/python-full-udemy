class Carro:
    def __init__(self, nome):
        self.nome = nome
    def acelerar (self):
        print(self.nome,' está acelerando')


fusca = Carro('Fusca')
celta= Carro('Celta')
print(celta.nome)
celta.acelerar()

print(fusca.nome)