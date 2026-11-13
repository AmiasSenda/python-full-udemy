#escopo da class

class materialDigital:
    def __init__(self,nome):
        self.nome = nome

        marca = 'Apple'

    def status (self, estado):
        print('Material Digital: ',self.nome)
        print('Status actual - ',estado)


material =materialDigital('Computador Portátil')


#print(material.nome)
material.status('Disponível')
print()