class Escritor:
    def __init__(self,nome):
        self.nome = nome

class FerramentaDeEscrever:
    def __init__(self,nomeF):
        self.nomeF = nomeF

    def escrever (self):
        return self.nome,' está a escrever'



Autor = Escritor('Amias Senda')

print(FerramentaDeEscrever.escrever(Autor))
