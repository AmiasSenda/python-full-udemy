def criar_funcao(func):
    def interna (*args, **kwargs):
        print('Vou te decorar')

        for arg in args:
            checkarString(arg)
        resultado = func(*args, **kwargs)
        print('O seu resultado foi: ',resultado)
        print('Ok, agora você foi decorada')

        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string [::-1]


def checkarString (param):
    if not isinstance(param, str):
        raise TypeError('parametro deve ser uma string')


#inverter = criar_funcao(inverte_string)

invertida = inverte_string('123')

print(invertida)