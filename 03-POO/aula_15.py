class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print("Estou no GETTER")
        return self._cor
   
    @cor.setter
    def cor(self,conteudo):
        print("Estou no SETTER")
        if conteudo == 'Amarelo':
            raise ValueError('Não quero esta collor')
        self._cor = conteudo
        self._cor_tampa = conteudo
        
    @property
    def cor_tampa(self):
        return self._cor_tampa
        

caneta = Caneta('Azul')
caneta.cor = 'vermelho'
caneta._cor_tampa ='Branco'

print(caneta.cor) 
print(caneta.cor_tampa)  
print() 