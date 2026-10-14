# META CARACTERES:  ^ $ * + ? { } \ ( )

# + Quantificador - 0 ou n
# * Quantificador - 1 ou n
# ? Quantificador - 1 ou 0
# ()
#{n}
#{min, max}

import re


texto = '''
João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de João. Teve 5 filhos, todos adultos atualmente.
Maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Jooooooooooooãoooooooo, o café tá prontinho aqui. Veeemm! veemmm vem"
jã

'''

print(re.findall(r'Jo+ão+',texto, flags=re.I)) 


print(re.sub(r'Jo+ão+', 'Marcos', texto, flags=re.I))

print(re.sub(r'Jo*ão*', 'Marcelo', texto, flags=re.I))


print(re.sub(r'jo?ão','Baby',texto, flags=re.I))

print(re.findall(r'jo{1,}ão{1,}',texto,flags=re.I)) # Intervalo de letras
print(re.findall(r've{1,3}m{1,2}',texto,flags=re.I)) # Intervalo de letras 

texto2= 'João Ama ser amado'

print(re.findall(r'ama[a-zA-Z]{0,}',texto2,flags=re.I))