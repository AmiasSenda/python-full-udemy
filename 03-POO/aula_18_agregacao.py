class Carrinho:
    def __init__(self):
        self._produtos= []

    def total (self):
        return sum ([p.preco for p in self._Produtos])

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome,produto.preco)
        print()


