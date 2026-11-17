class Escritor:
    def __init__(self,nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta (self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self,nome):
        self.nome = nome

    def escrever (self):
        return self.nome,' está a escrever'



Autor = Escritor('Amias Senda')
caneta = FerramentaDeEscrever('Caneta Bravo')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
Autor.ferramenta = caneta
Autor.ferramenta = maquina_de_escrever

print(maquina_de_escrever.escrever())
print(caneta.escrever())

print()
#print(FerramentaDeEscrever.escrever(Autor))
