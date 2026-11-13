import json
from aula_08 import CAMINHO_ARQUIVO, Pessoa, fazer_dump

fazer_dump()
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas  = json.load(arquivo)
    
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])


    print('Nome: ',p1.nome,'idade: ',p1.idade)
    print('Nome: ',p2.nome,'idade: ',p2.idade)
    print('Nome: ',p3.nome,'idade: ',p3.idade)
