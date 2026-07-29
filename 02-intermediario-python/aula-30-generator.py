def generator (n=0): 
    yield 5
    print('Continuar...')
    yield 3
    print('Mais uma...')
    yield 1
    print('vou terminar...')
    return 'ACABOU'
gen = generator(n=0)

for n in gen:
    print(n)


def generator2 (n=0, maximum=10):
    while True:
        yield n

        if n >= maximum:
            return
        n+=1


gen = generator2()

for n in gen:
    print(n)