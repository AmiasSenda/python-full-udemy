def executa (funcao, *args):
    return funcao(*args)


duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print(duplica(3))

#Outra forma de multiplica com o lambda

print(
    executa(
        lambda x,y: x + y,
        3,3
    ),
    #Essa função aqui vai somar.
)
