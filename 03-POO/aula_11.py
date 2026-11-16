#method & @classmethod vs @staticmethod
#method - self, metodo de instância
#@classmethod - cls,método de classe
#@staticmethod - método estático (sem Self, sem cls)


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self,user):
        self.user = user
    def  set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        


c1 = Connection()
c1.set_user('Amias')
c2 = Connection()
c2.set_password('A.Ml')
print('user: ',c1.user)
print('password: ',c2.password)
print()
