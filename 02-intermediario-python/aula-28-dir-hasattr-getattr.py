string = 'Amias'
string2 = 'Coisa Permanente'

if hasattr (string, 'upper'):
    print('Existe o método upper')
    print(string.upper())


metodo = 'uppe4r'
print()

if hasattr (string2,metodo):
    print('Existe o método upper')
    print(getattr(string2,metodo)())
else:
    print('não existe este método')
