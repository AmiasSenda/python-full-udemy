s1 = set()

s1.add('Amias')
s1.add(1)
s1.add('Blá Blá Blá')

print(s1)

s1.update(('Olá mundo!', 3,4,5,67))
print()
print(s1)

#s1.clear() - elimina tudo que está no set.

#s1.discard() - elimina que colocares dentro de parentes


s1.discard(1)

print(s1)