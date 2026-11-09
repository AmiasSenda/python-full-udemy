class Pessoa:
    nome = 'Amias Senda'
    nascimento = '2000/07/01'
    genero = 'F'
    nivelAcademic = 'Engenheira Informática'

class Pessoa0:
    nome0 = 'Lucinda Gaio'
    nascimento0 = '2004/04/12'
    genero0 = 'F'
    nivelAcademic0 = 'Engenheira Informática'

p1 = Pessoa()
p0 = Pessoa0()
print('DADOS PESSOAIS: ')
print('Nome completo: ',p1.nome)
print('Data de nascimento: ', p1.nascimento)
print('Gênero: ',p1.genero)
print('Status acadêmico: ',p1.nivelAcademic)
print()