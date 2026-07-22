total = 0
print('Questão 1: Quanto é 2 + 2 ?')
print('Opções: ')
print('A)-1')
print('B)-3')
print('C)-8')
print('D)-4')
v1 = input('Escolha uma das alinhas:  ')
if(v1 == 'D'):
    print('ACERTOU!')
    total +=1
else:
    print('ERROU!')

print('Questão 2: Quanto é 5 * 5 ?')
print('Opções: ')
print('A)-25')
print('B)-55')
print('C)-50')
print('D)-10')
v1 = input('Escolha uma das alinhas:  ')
if(v1 == 'A'):
    print('ACERTOU!')
    total +=1
else:
    print('ERROU!')

print('Questão 1: Quanto é 10/2 ?')
print('Opções: ')
print('A)-10')
print('B)-4')
print('C)-5')
print('D)-3')
v1 = input('Escolha uma das alinhas:  ')
if(v1 == 'C'):
    print('ACERTOU!')
    total +=1
else:
    print('ERROU!')


print()
print('você acertou',total,' de 3 perguntas!')