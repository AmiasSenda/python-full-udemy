#Função lambda - é uma função como qualquer outra em Python,
#  porém são funções anônimas que contêm apenas uma linha.
# Na Função Lambda tudo deve ser contido dentro de uma única expressão.

#lista = [4,32,1,34,5,6,6,21]

#print(lista)
#lista.sort(reverse=True)

lista = [
    {'nome': 'Luiz','sobrenome':'miranda'},
    {'nome': 'Amias','sobrenome':'Senda'},
    {'nome': 'Daniel','sobrenome':'António'},
    {'nome': 'Rewdane','sobrenome':'Jacline'},
]
    
#lista.sort(key=lambda item: item['nome'])

def exibir (lista):
    for item in lista:
        print(item)
    print()

l1= sorted(lista, key=lambda item: item['nome'])
l2= sorted(lista, key=lambda item: item['sobrenome'])


exibir(l1)
exibir(l2)


