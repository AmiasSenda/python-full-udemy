lista1 = ['Salvador', 'Ubatuba','Belo Horizonte']
lista2 = ['BA', 'SP','MG','RG']
lista3 = []
if lista1 < lista2:
    print('lista1 é menor!')
    for i in lista2:
        lista3 = list(zip(lista1,lista2))
else:
    print('lista2 é menor!')
    for i in lista2:
            lista3 = list(zip(lista1,lista2))


print(lista3)