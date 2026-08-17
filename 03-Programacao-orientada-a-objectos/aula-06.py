from datetime import datetime


class Pessoa:
    ano_actual = 2026

    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def get_ano_nasc (self):
        return Pessoa.ano_actual - self.idade



p1 = Pessoa('Amias Senda',2000)
print(p1.get_ano_nasc())
print('Ano actual: ',Pessoa.ano_actual)
Pessoa.ano_actual = 2100
print(p1.get_ano_nasc())

alterar_nome = p1.__dict__['nome'] = 'Adilson Fuxe'

print(p1.__dict__)
print(alterar_nome)

del p1.__dict__['nome']

print(p1.__dict__)