class Carrinho:
    def __init__(self):
        self._produtos= []

    def total (self):
        return sum ([p.preco for p in self._Produtos])

    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)


    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome,produto.preco)
        print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()

p1,p2,p3 = Produto('Banana',500.55), ('Morango',1050.44),('Pêssego',875.77)
        
print(carrinho.listar_produtos())