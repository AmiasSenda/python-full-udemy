import json 

caminho_arquivo = 'aula-08.json'


class Pessoa:
    def __init__(self,nome,idade):
        self.nome= nome
        self.idade = idade
        pass


p1 = Pessoa('Amias Senda',26)
p2 = Pessoa('Madalena Saraiva',31)
p3 = Pessoa('Miriam Nabi',24) 

bd = [vars(p1),p2.__dict__,vars(p3)]

with open(caminho_arquivo,'w') as arquivo:
    json.dump(bd,arquivo, ensure_ascii=False,indent=2)