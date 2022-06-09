from abc import abstractclassmethod,ABC


class Veiculos:
    """Classe Veiculo"""
    def __init__(self,dono,marca_veiculo):
        self.dono=dono
        self.marca_veiculo=marca_veiculo
        self.motor=0

class Motor:
    """Classe Motor"""
    def __init__(self,marca,potencia):
        self.marca=marca
        self.potencia=potencia


class Motor_Eletrico(Motor):
    """Classe Motor Eletrico-> Herda de Motor"""
    def __init__(self, marca,potencia):
        super().__init__(marca,potencia)


class Motor_Cobustao(Motor):
    """Classe Motor Combusão-> Herda de Motor"""
    def __init__(self, marca,potencia):
        super().__init__(marca,potencia)


class Motor_Hibrido(Motor):
    """Classe Motor Hibrido-> Herda de Motor"""
    def __init__(self, marca,potencia):
        super().__init__(marca,potencia)


class Caminhao(Veiculos):
    """Classe Motor Caminhão-> Herda de Veiculo"""
    def __init__(self, dono, marca_veiculo):
        super().__init__(dono, marca_veiculo)

    def printar_veiculo(self):
        print(f"Dono: {self.dono}")
        print(f"Tipo: {self.__class__.__name__}")
        print(f"Marca do Veiculo: {self.marca_veiculo}")
        print(f"Marca do Motor: {self.motor.marca}")
        print(f"Tipo do Motor: {self.motor.__class__.__name__}")
        print(f"Potencia: {self.motor.potencia}")


class Carro(Veiculos):
    """Classe Motor Caminhão-> Herda de Veiculo"""
    def __init__(self, dono, marca_veiculo):
        super().__init__(dono, marca_veiculo)

    def printar_veiculo(self):
        print(f"Dono: {self.dono}")
        print(f"Tipo: {self.__class__.__name__}")
        print(f"Marca do Veiculo: {self.marca_veiculo}")
        print(f"Marca do Motor: {self.motor.marca}")
        print(f"Tipo do Motor: {self.motor.__class__.__name__}")
        print(f"Potencia: {self.motor.potencia}")


class Moto(Veiculos):
    """Classe Motor Caminhão-> Herda de Veiculo"""
    def __init__(self, dono, marca_veiculo):
        super().__init__(dono, marca_veiculo)
        
    def printar_veiculo(self):
        print(f"Dono: {self.dono}")
        print(f"Tipo: {self.__class__.__name__}")
        print(f"Marca do Veiculo: {self.marca_veiculo}")
        print(f"Marca do Motor: {self.motor.marca}")
        print(f"Tipo do Motor: {self.motor.__class__.__name__}")
        print(f"Potencia: {self.motor.potencia}")





class Creator_Veiculo(ABC):
    @abstractclassmethod
    def criar_veiculo(self):
        pass


class Creator_Motor(ABC):
    @abstractclassmethod
    def criar_motor(self):
        pass

class Carro_Factory(Creator_Veiculo):
    """Fábrica do Carro"""
    def __init__(self,dono,marca_veiculo):
        self.dono=dono
        self.marca_veiculo=marca_veiculo
    
    def criar_veiculo(self) -> Veiculos:
            return Carro(self.dono,self.marca_veiculo)


class Moto_Factory(Creator_Veiculo):
    """Fábrica da Moto"""
    def __init__(self,dono,marca_veiculo):
        self.dono=dono
        self.marca_veiculo=marca_veiculo
    
    def criar_veiculo(self) -> Veiculos:
            return Moto(self.dono,self.marca_veiculo)

class Caminhao_Factory(Creator_Veiculo):
    """Fábrica da Moto"""
    def __init__(self,dono,marca_veiculo):
        self.dono=dono
        self.marca_veiculo=marca_veiculo
    
    def criar_veiculo(self) -> Veiculos:
            return Caminhao(self.dono,self.marca_veiculo)


class Motor_Eletrico_Factory(Creator_Motor):
    """Fábrica do Motor"""
    def __init__(self,marca_motor,potencia):
        self.marca_motor=marca_motor
        self.potencia=potencia

    
    def criar_motor(self) -> Motor:
        return Motor_Eletrico(self.marca_motor,self.potencia)


class Motor_Combustao_Factory(Creator_Motor):
    """Fábrica do Motor"""
    def __init__(self,marca_motor,potencia):
        self.marca_motor=marca_motor
        self.potencia=potencia

    
    def criar_motor(self) -> Motor:
        return Motor_Cobustao(self.marca_motor,self.potencia)


class Motor_Hibrido_Factory(Creator_Motor):
    """Fábrica do Motor"""
    def __init__(self,marca_motor,potencia):
        self.marca_motor=marca_motor
        self.potencia=potencia

    
    def criar_motor(self) -> Motor:
        return Motor_Hibrido(self.marca_motor,self.potencia)



Carro1=Carro_Factory("Gabriel","Ferrari").criar_veiculo()
Carro1.motor=Motor_Combustao_Factory("GM","250cv").criar_motor()
Carro1.printar_veiculo()

print("----------------------------------------------------------")
Caminhao1=Caminhao_Factory("João","Fiat").criar_veiculo()
Caminhao1.motor=Motor_Hibrido_Factory("GM","250cv").criar_motor()
Caminhao1.printar_veiculo()


print("----------------------------------------------------------")
Moto1=Moto_Factory("Felipe","Mercedes").criar_veiculo()
Moto1.motor=Motor_Eletrico_Factory("GM","250cv").criar_motor()
Moto1.printar_veiculo()