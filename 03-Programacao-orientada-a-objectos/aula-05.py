class Camera:
    def __init__(self,nome,filmar=False):
        self.nome = nome
        self.filmar = filmar

    def filmar1(self):
        print(self.nome, 'está filmando...')
        self.filmar= True
    def fotografar(self):
        if self.filmar:
            print(self.nome,'Não pode fotografar e filmar aomesmo tempo')

        print(self.nome,'Está filmando')


c1 = Camera('Canon')
c2=Camera('Sony')
c1.filmar1()
c1.fotografar()