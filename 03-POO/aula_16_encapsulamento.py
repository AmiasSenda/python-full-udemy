

from functools import partial


class Foo:
    def __init__(self):
        self.public ='Este negócio é público'
        self._protected ='Isso é Protegido'
        self.__exemplo = 'Isto é PRIVATE'
        self._metodo_protected()


    def metodo_publico(self):
        print(self.__exemplo)
        return 'método Público'
   
    
    def _metodo_protected(self):
        print('PROTECTED!')
        print()
        return 'metodo Protegido'
    def __metodo_private(self):
        print('MÉTODO PRIVATE')
        return 'private'    

f = Foo()
print(f.public)
print(f._protected)
print(f.metodo_publico())
print(f._metodo_protected())
print(f._Foo__metodo_private())
print(f._Foo__exemplo)
print()