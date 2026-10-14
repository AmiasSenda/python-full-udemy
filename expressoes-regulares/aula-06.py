import re 
nif = '''
005559939LA048
'''


print(re.findall(r'^[0-9]{3}$',nif))
print('SÓ LETRAS: ',re.findall(r'[^0-9]+',nif)) #SÓ QUERO LETRAS
print('SÓ NÚMEROS: ',re.findall(r'[^A-Z]+',nif)) #SÓ QUERO NÚMEROS
