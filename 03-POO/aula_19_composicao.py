class Cliente:
    
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua,numero):
        for adress in rua,numero:
            self.enderecos.append()

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)


class Adress:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero



cliente1 =Cliente('Amias Senda')
cliente1.inserir_endereco('Av Brasil', 111)
cliente1.inserir_endereco('Rua J', 54)


#cliente1.listar_enderecos()




