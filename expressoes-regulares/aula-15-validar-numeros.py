import re
from pprint import pprint


numeros = '''
-987.654.321.000
5
128
-0,25
1.234.567.890
-3
125.789
0,7
-18.630
7.542
-946
-987.654
10..2
abn123
456A
++1213

'''


def is_float(string):
    return bool(re.fullmatch(r'^[+-]?\d+(?:\.\d+)?$',string))

def is_int(string):
    return bool(re.fullmatch(r'^[+-]?\d+$',string))


print(is_int('-124.6'))

regex1 = re.compile(r'^[+-]?\d+(?:\.\d+)?$', flags=re.MULTILINE)
regex2 = re.compile(r'^[+-]?\d+$', flags=re.MULTILINE)

print(regex1.findall(numeros))
print()
print(regex2.findall(numeros))

while True:
    numero = input('digite um número: ')
    
    

    if (is_int(numero)):
            numeroF = int(numero)
            print('O Número: ',numeroF,' é um número do tipo  inteiro.')
            continue
    if (is_float(numero)):
        numeroF = float(numero)
        print('O Número: ',numeroF,' é um número do tipo  float.')
        continue