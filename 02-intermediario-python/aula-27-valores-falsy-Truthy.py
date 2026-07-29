lista = [] # Uma lista vazia é Falsy 
dicionario = {}  # É Falsy
conjunto = set () #  É Falsy
tupla = ()  # É Falsy
string = '' # É Falsy
inteiro = 0 # É Falsy
flutuante = 0.0 # É Falsy
nada = None # É Falsy
Falso = False # É Falsy
intevalo = range (0) # É Falsy
...


def falsy (valor):
    return 'falsy ' if not valor else 'truthy'


print(f'TESTE', falsy('TESTE'))

print(lista, falsy(lista))
print(dicionario, falsy(dicionario))
print(nada, falsy(nada))
print(conjunto, falsy(conjunto))
print(tupla, falsy(tupla))
print(inteiro, falsy(inteiro))
print(flutuante, falsy(flutuante))
print(Falso, falsy(falsy))
print(intevalo, falsy(intevalo))
print(string, falsy(string))
