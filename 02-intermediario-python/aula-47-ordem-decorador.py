def paramentros_decorador(nome):
    def decorador(func):
        print('Decorador: ',nome)

        def sua_nova_funcao (*args, **kwargs):
            res = func(*args, **kwargs)
            final ='Soma: ' ,res,' Nome: ',nome
            return final
        return sua_nova_funcao
    return decorador


@paramentros_decorador(nome='primeiro')
def soma(a,b):
    return a+b

print(soma(2,3))