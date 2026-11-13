
import json
CAMINHO_ARQUIVO= 'aula_08.json'


class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Amias', 28)
p2 = Pessoa('Esposo', 30)
p3 = Pessoa('Filho', 1)
bd =  [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('DUMP')
        print()
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)