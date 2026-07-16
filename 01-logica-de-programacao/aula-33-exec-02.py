entrada = input('que horas são ? ')


try:
    hora = int(entrada)

    manha = (hora >= 0)  and (hora < 12)
    tarde = (hora >= 11) and (hora <= 17)
    noite = (hora >= 18)and (hora < 24)
    print()
    print('........................................')
    if manha:
        print('Bom dia!')
    elif tarde:
        print('Boa Tarde!')
    elif noite:
        print('Boa Noite!')
    else:
        print('Horário Inexistente!')

    print()
except:
    print('por favor digite apenas númerpos inteiros')