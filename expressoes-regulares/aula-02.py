# META CARACTERES: . ^ $ * + ? { } \ |( )

# | OU
# [] Conjunto de caracteres

import re
texto = '''
João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de João. Teve 5 filhos, todos adultos atualmente.
Maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Jooooooooooooãoooooooo, o café tá prontinho aqui. Veeemm!"
'''


print(re.findall(r'João|Maria|ad.....',texto))
print(re.findall(r'João|Maria|ad.....',texto))


print(re.findall(r'[Jj]oão|Maria',texto))
print(re.findall(r'[a-zA-Z0-9]aria',texto))

# IMPORTANTE - NÃO DIFERENCIAR MAIÚSCULAS E MINÚSCULAS
print()
print('Com o Flag: IGNORECASE: ',re.findall(r'JoãO|mArIa',texto, flags=re.I))
