import re

texto2 = 'O João gosta de mulheres' \
'  E adora ser mimado'


print (re.findall(r'^o.*o$',texto2, flags=re.I | re.S))# PEGA A FRASE QUE COMEÇA COM E TERMINA COM UMA LETRA.