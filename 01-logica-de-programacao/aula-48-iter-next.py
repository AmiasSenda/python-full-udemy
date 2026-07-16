texto = 'Amias'

iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break


print()