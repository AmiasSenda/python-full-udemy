
# re.A
# re.I
# re.M
# re.S

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

semAcento = (re.findall(r'[a-zA-Z0-9]+',texto)) # CONSIGO PEGAR TODAS AS PALAVRAS E NÚMEROS SEM ACENTUAÇÃO.
comAcento = (re.findall(r'\w+',texto)) # CONSIGO PEGAR TODAS AS PALAVRAS E NÚMEROS COM ACENTOS TAMBÉM.

semAcento02= (re.findall(r'\w+', texto, flags=re.A)) #PEGA AS PALAVRA SEM ACENTUAÇÃO.
pegarNumeros= (re.findall(r'\d+', texto)) #PEGA OS NÚMEROS QUE ESTÃO NO TEXTO.
#print(re.findall(r'\D+', texto)) #PEGA TUDO MENOS OS NÚMEROS QUE ESTÃO NO TEXTO.
print()
pegarTodosEspacosVazios= (re.findall(r'\s',texto)) # pega todo o espaço.
pegarTudoQueNaoEEspaco= (re.findall(r'\S+', texto)) # pega tudo que não é espaço.
pegarPalavrasComUmaInicial= (re.findall(r'\be\w+', texto,flags=re.I)) #PEGA TODAS AS PALAVRAS QUECOMEÇAM COM A LETRA INSERIDAS
pegarPalavrasQueTerminaCom= (re.findall(r'\w+e\b', texto,flags=re.I)) # PEGA TODAS AS PALAVRAS QUE TERMINAM COM A LETRA INSERIDA.



'''print('PALAVRAS QUE INICIAM COM [E]: ',pegarPalavrasComUmaInicial)
print()
print('PALAVRAS QUE TERMINAM COM [E]: ',pegarPalavrasQueTerminaCom)
print()
'''
print()
print(re.findall(r'\b\w{4}\b',texto, flags=re.I)) # pegar palavras só com 4 letras

print(re.findall(r'flo\B',texto, flags=re.I)) # SEM BORDA




print()