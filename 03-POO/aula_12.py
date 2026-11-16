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
        connection.user = user
        connection.password = password
        return connection
        
    @staticmethod
    def log(msg):
        print('LOG: ',msg)

c1 = Connection.create_with_auth('Amias','#@...')
print('user: ',c1.user)
print('password: ',c1.password)
print(Connection.log('Esta é a ,mensagem de LOG'))
print()
