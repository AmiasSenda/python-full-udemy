class Pessoa:
    ano = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod
    def metodo_de_classe(cls):
        print('Hey Hey')
   
    @classmethod
    def outra_class_estranha(cls,nome):
        return cls(nome, 32)

    @classmethod
    def outra_class(cls,nome,idade):
        return cls(nome,idade)


p2 = Pessoa.outra_class_estranha('Amias')
print(p2.nome, p2.idade)
p3 = Pessoa('Anônima',23)
print(p3.nome, p3.idade)





Pessoa.metodo_de_classe()