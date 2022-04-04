class Eletronico:


    """Classe Eletronico: Tudo que use eletricidade para funcionar"""
    def __init__(self,nome,ligado):
        """Construtor"""
        self.nome=nome
        self.ligado=ligado


    def ligar(self):
        """Liga o aparelho"""
        if not self.ligado:
            self.ligado=True


    def desligar(self):
        """Desiga o aparelho"""
        if self.ligado:
            self.ligado=False


class Carro:


    """Classe Carro"""
    def __init__(self,modelo,marca,dono,movimentando):
        self.modelo=modelo
        self.marca=marca
        self.dono=dono
        self.movimentando=movimentando


    def parar(self):
        """Para o carro"""
        if self.movimentando:
            self.movimentando=False


    def andar(self):
        """Faz o carro se mover"""
        if not self.movimentando:
            self.movimentando=True


class Carro_eletrico(Carro, Eletronico):


    def __init__(self,carga_bateria, modelo, marca, dono, movimentando,ligado):
        Carro.__init__(self,modelo,marca,dono,movimentando)
        Eletronico.__init__(self,modelo,ligado)
        self.carga_bateria=carga_bateria


    def recarregar(self):
        """Carrega a bateria do carro"""
        #Parar o carro (método super refere-se a primeira classe)
        super().parar() 
        #Desligar o carro
        Eletronico.desligar(self)
        self.carga_bateria=100

if __name__== '__main__':
    """Main para mostrar a funcionalidade"""
    C1=Carro_eletrico(50,"X1","Tesla","Gabriel",True,True)
    print(f"Ligado:{C1.ligado}")
    print(f"Movimento:{C1.movimentando}")
    print(f"Carga:{C1.carga_bateria}")
    print("\n###############################\n")
    C1.recarregar()
    print(f"Ligado:{C1.ligado}")
    print(f"Movimento:{C1.movimentando}")
    print(f"Carga:{C1.carga_bateria}")


    
