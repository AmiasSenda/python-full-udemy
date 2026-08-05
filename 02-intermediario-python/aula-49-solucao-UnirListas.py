def zipper(lista1,lista2):
    valor_min= min(len(lista1),len(lista2))
    return[(lista1[i],lista2[i]) for i in range(valor_min)]


l1 = ['Salvador', 'Ubatuba','Belo Horizonte']
l2 = ['BA', 'SP','MG','RG']


print(zipper(l1,l2))



