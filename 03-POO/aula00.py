class Pessoa:
    nome = 'Amias Senda'
    nascimento = '2000/07/01'
    genero = 'F'
    nivelAcademic = 'Engenheira Informática'

class Pessoa0:
    def __init__(self,nome,nascimento ):
        nomeA = nome
        data = nascimento


p1 = Pessoa()
p0 = Pessoa0(p1.nome, p1.nascimento)
print('DADOS PESSOAIS: ')
print('Nome completo: ',p1.nome)
print('Data de nascimento: ', p1.nascimento)
print('Gênero: ',p1.genero)
print('Status acadêmico: ',p1.nivelAcademic)
print()