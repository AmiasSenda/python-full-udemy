class Carrinho:
    def __init__(self):
        self._produtos= []

   
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)


    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()
    
    
    def total (self):
            return sum (p.preco for p in self._produtos)
    

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()

p1= Produto('Banana',500.55)
p2= Produto('Morango',1050.44)
p3= Produto('Pêssego',875.77)
carrinho.inserir_produtos(p1,p2,p3)
carrinho.listar_produtos()
print('Total: ',carrinho.total(),'KZS')
print()