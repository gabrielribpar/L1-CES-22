from abc import abstractclassmethod


class Bolo:
    def __init__(self,tipo, calda):
        self.tipo=tipo
        self.calda=calda



class Bolo_Factory:
    def __init__(self,tipo, calda):
        self.tipo=tipo
        self.calda=calda

    @abstractclassmethod
    def criar_bolo(self):
        pass


class Bolo_Aniversario_Factory(Bolo_Factory):
    def __init__(self,calda):
        self.tipo="Aniversário"
        self.calda=calda

    def criar_bolo(self):
        return Bolo(self.tipo,self.calda)

class Bolo_Festa_Factory(Bolo_Factory):
    def __init__(self,calda):
        self.tipo="Festa"
        self.calda=calda

    def criar_bolo(self):
        return Bolo(self.tipo,self.calda)

class Bolo_Casamento_Factory(Bolo_Factory):
    def __init__(self,calda):
        self.tipo="Casamento"
        self.calda=calda

    def criar_bolo(self):
        return Bolo(self.tipo,self.calda)

class Bolo_Informal_Factory(Bolo_Factory):
    def __init__(self,calda):
        self.tipo="Informal"
        self.calda=calda

    def criar_bolo(self):
        return Bolo(self.tipo,self.calda)
        


Bolo=Bolo_Informal_Factory("Chocolate")
print(Bolo.tipo,Bolo.calda)