class Pessoa:
    atributo = 'valor'

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        return 2026 - self.idade


p1=Pessoa('Amias',26)
p2 = Pessoa('Lucinda',23)

print('Ano de nascimento: ',p1.get_ano_nascimento())
print('Ano de nascimento: ',p2.get_ano_nascimento())
