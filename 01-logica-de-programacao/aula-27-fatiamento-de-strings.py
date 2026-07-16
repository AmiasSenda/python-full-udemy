v = 'hello word!'
print(v[::-1])
nome = input('digite o seu nome: ')
if nome != '':
    print()
    print('..............................................')
    print('Seu nome: ',nome)
    print('seu nome invertido: ',nome[::-1])
    if  ' ' in nome:
        print('seu nome contem espaços em branco')
    else:
        print('seu nome não contém espaços em branco')
    print('seu nome tem: ', len(nome))
    print('Sua primeira letra: ', nome[0])
    ult = nome [::-1]
    print('Sua ultima letra: ', nome[-1])
    print()
else:
    print("desculpe mas não digitou nada!")

    print()