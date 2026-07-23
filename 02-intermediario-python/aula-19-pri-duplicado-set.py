lista_de_inteiros = [
    [1,2,3,4,1,5,6,7,3,8],
    [4,5,6,7,8,3,5,7,8,9]
    ]

def encontra_primeiro_duplicado(lista_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_inteiros:
    print(lista,encontra_primeiro_duplicado(lista))