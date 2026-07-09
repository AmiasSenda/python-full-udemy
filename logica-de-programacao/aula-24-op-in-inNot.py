nome = 'Amias'
print(nome[4])
print("")
print('as' in nome) #'as' está em Amias ? sim.
print('bs' not in nome) # 'bs' está em Amias ? Não

nomeUtil = input('Digite o seu nome: ')
encontrar = input('digite o que deseja encontrar: ')
print("")
print("")

if encontrar in nomeUtil:
    print(f'{encontrar} está em {nomeUtil}')
else:
    print(f'{encontrar} não está em {nomeUtil}')

print("")
print("")