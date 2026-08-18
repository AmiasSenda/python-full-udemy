class Foo:
    def __init__(self):
        self.public ='isso é público'
        self._protected = 'Isso está protegido'

        self._metodo_protected()

    def metodo_publico(self):
        return 'Método público'

    def _metodo_protected (self):
        print('_method protected')
        return 'Method protected'
    def __methodA(self):
        print('privado')
        return 'Restrito'
 

f= Foo()


print(f.public)
print(f._protected)
print(f._Foo__methodA( ))