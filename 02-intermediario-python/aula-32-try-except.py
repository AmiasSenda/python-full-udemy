
try:
    a = 18
    b = 1
    print('Linha 01')
    c = a/b + 'b'
    print('Linha 02')
except ZeroDivisionError:
    print("Dividiu por Zero")
except NameError:
    print('Uma variavel {b} não está definido')
except TypeError:
    print('TypeError')
except Exception:
    print('Erro Desconhecido')