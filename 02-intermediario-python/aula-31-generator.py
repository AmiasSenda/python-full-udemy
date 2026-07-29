def gen():
    print('COMEÇOU GN - 0')
    yield 1
    yield 3
    yield 5

def gen0(gn):
   
    yield from gn()
    print('COMEÇOU GN - 2')
    yield 7
    yield 9
    yield 0

def gen1():
    print('COMEÇOU GN - 3')
    yield 2
    yield 4
    yield 6

g = gen0(gen)
g1 = gen0(gen1)

for num in g:
    print(num)
for num in g1:
    print(num)