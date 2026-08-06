#Count contador sem fim está no método itertools.


from itertools import count

c1 = count(8,8)
c2 = count()
r1= range(2,10)

print('c1', hasattr(c1, '__iter__'))

for i in c1:
    if i >  100:
        break
    print(i)

print()
print('AS SENSAÇÕES')

for i in r1:
    print(i)

print('PAREI')