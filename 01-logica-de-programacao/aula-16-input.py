#input: me permite receber um valor do utilizador.

from datetime import datetime
nome = input('digite o seu nome: ')
AnoNasc = int (input('digite o seu ano de nascimento: '))
print()
data = datetime.now()

anoct = data.year
idade = int(anoct) - AnoNasc
print(f'Prazer, {nome}!')
print(f'Sua idade actual: {idade}')

if(idade >= 18):
     print('Tu és maior de idade.')
    
else:
        print('Tu és menor de idade.')

print()



