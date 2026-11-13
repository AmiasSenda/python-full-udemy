class Camera:
    def __init__(self, nome, estado=False):
        self.nome = nome
        self.estado = estado
    
    def filmar(self):

        print(self.nome, 'está a filmar')
        self.estado = True

camera_1 = Camera('Canon')
camera_2 = Camera('Sony')


camera_1.filmar()
camera_2.filmar()

