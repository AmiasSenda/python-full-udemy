
try:
    8/0
    print(111)
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('ERROR: Dividiu por 0')
else:
    print('Não deu erro')
finally:
    print()
    print('Anaaaaaaaaaaaaaaa')
    print()