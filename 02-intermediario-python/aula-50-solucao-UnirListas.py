from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba','Belo Horizonte']
l2 = ['BA', 'SP','MG','RG']

print (list(zip(l1,l2)))
print(list(zip_longest(l1,l2)))