 # *args - tem haver com os argumentos não nomeados.
def soma (*args): 
    tot = 0
    for numero in args:
        print('Total',tot,numero)
        tot = tot + numero
        print('Total', tot)


soma(1,2,3,4,5,6)

