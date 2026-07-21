"""
Funções são trechos de códigos
usados para replicar determinada 
ação ao longo do meu código.
Elas podem receber valores para 
parâmetros e retornar um valor específico...

"""

def teste (a):
    num1 = int(a)
    i = 1
    print()
    print('Eis a tabuada dos:  ',num1)
    print()
    while i <= 12:
        print (num1,' X ',i,' = ', num1 * i)
        i +=1

    print()


def saudacao (nome):
    n = nome
    print('Hi, ',n, 'you are very friendly!')
    print()


name = input('Digite o seu Nome: ')
tb = int(input('Digite um número: '))

teste(tb)
saudacao(name)
