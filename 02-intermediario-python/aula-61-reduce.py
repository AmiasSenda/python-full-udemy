
from functools import reduce


produtos= [
    {'nome':'Banana', 'preco':350.76},
    {'nome':'Laranja', 'preco':500.66},
    {'nome':'Manga', 'preco':650.70},
    {'nome':'Loengo', 'preco':540.60},
]

#Somar o total
#print(sum(p['preco'] for p in produtos))




total = reduce(
    lambda ac, p:ac + p['preco'],produtos,0)

print('Total: ',total)
print()





