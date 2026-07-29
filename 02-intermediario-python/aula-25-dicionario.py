produto = {
    'nome':'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}
#print(produto.items())

for chave,  itens in produto.items():
    ...
   # print(chave, ':', itens)


#COPIAR PPRODUTO PARA DC


    for chave,itens in produto.items():
      dc = produto.items()

#print(dc)

dc1 ={
   chave: valor.upper()
   if isinstance(valor, str) else valor 
   for chave,valor 
   in produto.items()
   if chave != 'categoria'
}

print(dc1)


#Pegar valores de uma lista que parecem um dicionário

lista = [
   ('a','valor a'),
   ('b','valor b'),
   ('c','valor c')
]

dc2 = {
        chave:valor 
        for chave, valor in lista
}

#print(dc2)

#CONVERTER UMA LISTA EM DICIONÁRIO QUE TENHA CHAVE E VALOR: 

print(dict(lista))


#SETCOMPEHENCTION

s1= { i for i in range(10)}

print(s1)
