import sys


iterable = ['I','like','watch TV', '__iter__']

iterator = iter(iterable)
#print(next(iterator))
lista = [n for n in range (10000)]
generator = ( n for n in range(10))


print(sys.getsizeof(generator))
print(sys.getsizeof(lista))