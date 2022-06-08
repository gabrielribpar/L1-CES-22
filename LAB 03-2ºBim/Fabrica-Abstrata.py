from abc import abstractclassmethod


class Bolo:
    """Classe Bolo"""
    def __init__(self,tipo, calda):
        self.tipo=tipo
        self.calda=calda



class Bolo_Factory:
    """Fábrica Abstrata para o Bolo"""
    def __init__(self,tipo, calda):
        self.tipo=tipo
        self.calda=calda

    @abstractclassmethod
    def criar_bolo(self):
        pass


class Bolo_Aniversario_Factory(Bolo_Factory):
    """Fábrica Concreta do bolo de aniversário"""
    def __init__(self,calda):
        self.tipo="Aniversário"
        self.calda=calda

    def criar_bolo(self):
        return Bolo(self.tipo,self.calda)


class Bolo_Festa_Factory(Bolo_Factory):
    """Fábrica Concreta do bolo de festa"""
    def __init__(self,calda):
        self.tipo="Festa"
        self.calda=calda

    def criar_bolo(self):
        return Bolo(self.tipo,self.calda)


class Bolo_Casamento_Factory(Bolo_Factory):
    """Fábrica Concreta do bolo de casamento"""
    def __init__(self,calda):
        self.tipo="Casamento"
        self.calda=calda

    def criar_bolo(self):
        return Bolo(self.tipo,self.calda)


class Bolo_Informal_Factory(Bolo_Factory):
    """Fábrica Concreta do bolo informal"""
    def __init__(self,calda):
        self.tipo="Informal"
        self.calda=calda

    def criar_bolo(self):
        return Bolo(self.tipo,self.calda)
        


Bolo=Bolo_Informal_Factory("Chocolate")
Bolo2=Bolo_Aniversario_Factory("Chocolate")
print("Primeiro Bolo Criado:")
print(Bolo.tipo,Bolo.calda)
print("Segundo Bolo Criado:")
print(Bolo2.tipo,Bolo2.calda)