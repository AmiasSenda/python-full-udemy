#Sem lista comprehension

lista = []

for num in range(10):
    lista.append(num)

#print(lista)


#Com list comprehension

lista1 = [
    num for num in range(10)
]
print(lista1)

print()
lista2 = [
    num*3 for num in range(10)
]
print(lista2)