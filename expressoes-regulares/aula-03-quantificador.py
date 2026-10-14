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
