def criar_multiplicar (multiplicador):
    def multiplicar (numero):
        return numero * multiplicador
    return multiplicar



duplicar = criar_multiplicar(2)
triplicar = criar_multiplicar(3)
quadruplicar = criar_multiplicar(4)
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

print()

