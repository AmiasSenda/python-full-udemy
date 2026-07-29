string = 'Amias'
print(isinstance(string,int))
try:
    a =  18
    b =  0

    print('linha 1 '[1000])

    c = a/b

    print('linha 2')

except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('mensagem: ',error)
    print('Nome: ',error.__class__.__name__)
