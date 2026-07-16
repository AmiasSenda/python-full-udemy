nome = input('digite o seu nome: ')


qt=len(nome)
print(qt)
quant = int(qt)

if(quant > 1):

    if quant <=4:
        print(nome,' seu nome é curto')
    elif (quant >=5) and (quant<=6):
        print(nome,' seu nome é normal')
    elif quant > 6:
        print(nome,' seu nome é muito longo')
else:
    print('Digite pelo penos uma letra')


print()