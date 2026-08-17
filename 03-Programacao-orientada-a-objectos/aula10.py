class  connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user (self,user):
        self.user= user
    def set_password(self,password):
        self.password = password
    @classmethod
    def create_with_auth(cls,user,password):
        connection = cls
        connection.user = user
        connection.password = password
        return connection
        




c1= connection.create_with_auth ('Senda','***')
print('user: ',c1.user)
print('password: ',c1.password)

