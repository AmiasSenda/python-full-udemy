class Pessoa:
    ano_actual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        return Pessoa.ano_actual - self.idade


p1 = Pessoa('Amias',26)
p1.__dict__['Sobrenome'] = 'Senda'
p1.__dict__['SobreNomeActual'] = 'Malanga'
print(p1.__dict__)#Consigo ver o dicionário p1,variavel e valor
print(vars(p1))#Consigo ver o dicionário p1,variavel e valor
print()
print(p1.nome)
print(p1.idade)