linha = 'tem certeza que quer "sair " do sistema ?'
print(linha)
entrada = input()

print()
if entrada == 'sim' :
    print("Até Mais!")
elif entrada == 'nao':
    print("Eu sabia que poderias permanecer!")

else:
    print('Não seja confuso(a)!')