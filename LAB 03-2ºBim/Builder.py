
from abc import abstractclassmethod
from distutils.command.build import build


class Bolo:
    """Classe Bolo"""
    def __init__(self,tipo="Infomal",calda="Chocolate"):
        self.tipo=tipo
        self.calda=calda

class Interface_Bolo_Builder:
    @abstractclassmethod
    def build_calda(self,calda):
         pass
    @abstractclassmethod
    def build_tipo(self,tipo):
        pass

    @abstractclassmethod
    def resultado(self):
        pass


class Bolo_Builder(Interface_Bolo_Builder):
    """Builder do Bolo"""
    def __init__(self):
        self.calda="Chocolate"
        self.tipo="Informal"

    def build_calda(self,calda):
        "Constroi a calda"
        self.calda=calda
    def build_tipo(self,tipo):
        "Constroi o tipo"
        self.tipo=tipo
    def resultado(self):
        return Bolo(self.tipo,self.calda)

#Construir classes
Construir_Bolo=Bolo_Builder()
Bolo1=Construir_Bolo.resultado()
Construir_Bolo.build_calda("Morango")
Construir_Bolo.build_tipo("Casamento")
Bolo2=Construir_Bolo.resultado()

#Prints
print("Primeiro Bolo:")
print(Bolo1.tipo,Bolo1.calda)
print("Segundo Bolo:")
print(Bolo2.tipo,Bolo2.calda)