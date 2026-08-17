class Animal:
    def __init__(self,nome):
        self.nome = nome


        variavel = 'valor'
        print(variavel)
    def comer(self,alimento):
        return self.nome,' está comendo ',alimento

selvagem = Animal('Urso')
print(selvagem.nome)
print(selvagem.comer('Carne '))
