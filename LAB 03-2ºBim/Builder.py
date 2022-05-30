
from distutils.command.build import build


class Bolo:
    def __init__(self,tipo="Infomal",calda="Chocolate"):
        self.tipo=tipo
        self.calda=calda

class Bolo_Builder:
    def __init__(self):
        self.calda="Chocolate"
        self.tipo="Informal"

    def build_calda(self,calda):
        self.calda=calda
    def build_tipo(self,tipo):
        self.tipo=tipo
    def resultado(self):
        return Bolo(self.tipo,self.calda)

Construir_Bolo=Bolo_Builder()
Bolo1=Construir_Bolo.resultado()
Construir_Bolo.build_calda("Morango")
Construir_Bolo.build_tipo("Casamento")
Bolo2=Construir_Bolo.resultado()

print(Bolo1.tipo,Bolo1.calda)
print(Bolo2.tipo,Bolo2.calda)