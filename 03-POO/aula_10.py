#METODOS ESTÁTICOS EM PYTHON


class ClassA:
    
    @staticmethod
    def funcao(*args, **kwargs):
        print('Hey Hey', args, kwargs)

def funcao1(*args, **kwargs):
    print('Hey', args, kwargs)


c1 = ClassA()
c1.funcao(1,2,3)
funcao1(1, 2, 3)
ClassA.funcao(nomeado=1)
funcao1(nomeado=1)
    