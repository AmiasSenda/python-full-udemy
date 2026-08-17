class Pessoa:
    ano = 2023
    def __init__(self,nome,idade):
        self.nome =  nome
        self.idade = idade
    @classmethod 
    def metodo_de_class(cls):
        print('Hey')

    @classmethod
    def criar_35_anos(cls,nome):
        return cls(nome,35)
    @classmethod
    def anonimo(cls,idade):
        return cls('Anônima',idade)



p1 = Pessoa('Ana',50)
print(Pessoa.ano)
p1.metodo_de_class()
p2= Pessoa.criar_35_anos('Amias Bento')
print(p2.nome,p2.idade)
p3 =Pessoa.anonimo(22)

print(p3.nome,p3.idade)