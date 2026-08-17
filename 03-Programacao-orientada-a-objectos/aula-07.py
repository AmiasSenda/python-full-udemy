class Pessoa:
    ano_actual = 2026
    def __init__(self,nome,idade):
        self.nome =  nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_actual - self.idade


p1 = Pessoa('Amias Senda',26)

print(vars(p1))

      
