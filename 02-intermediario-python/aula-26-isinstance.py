lista = ['a',1,1.1,True, 
         [0,1,2],(1,2),

         {0,1}, {'nome':'Amias'}
         ]

# isinstance: Significa é instância de.
informaction = 'isinstance: Significa é instância de'
print(informaction.upper())
print()

print(lista)
print()
for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item,set))


print()
print('STRINGS')
for item in lista:
    if isinstance(item, str):
        print(item, isinstance(item,set))
print()
print('Números inteiros ')
#Quero checar apenas os numéricos
for item in lista:
    if isinstance(item, (int,float)):
        print(item, "MULTIPLICAR POR DOIS: ",item *2)



