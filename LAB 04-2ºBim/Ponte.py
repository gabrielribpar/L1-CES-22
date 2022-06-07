class Veiculos:
    """Classe Veiculo"""
    def __init__(self,dono,marca_veiculo,marca_motor,tipo_motor,potencia):
        self.dono=dono
        self.marca_veiculo=marca_veiculo
        self.motor=Motor_Factory(marca_motor,tipo_motor,potencia).criar_motor()


class Veiculo_Factory:
    """Fábrica de Veiculo"""
    def __init__(self,dono,tipo_veiculo,marca_veiculo,marca_motor,tipo_motor,potencia):
        self.dono=dono
        self.tipo_veiculo=tipo_veiculo
        self.marca_veiculo=marca_veiculo
        self.marca_motor=marca_motor
        self.tipo_motor=tipo_motor
        self.potencia=potencia
    
    def criar_veiculo(self):
        if self.tipo_veiculo=="Carro":
            return Carro(self.dono,self.tipo_veiculo,self.marca_veiculo,self.marca_motor,self.tipo_motor,
            self.potencia)
        if self.tipo_veiculo == "Caminhão":
            return Caminhao(self.dono,self.tipo_veiculo,self.marca_veiculo,self.marca_motor,self.tipo_motor,
            self.potencia)
        if self.tipo_veiculo == "Moto":
            return Moto(self.dono,self.tipo_veiculo,self.marca_veiculo,self.marca_motor,self.tipo_motor,
            self.potencia)


class Motor_Factory:
    """Fábrica do Motor"""
    def __init__(self,marca_motor,tipo_motor,potencia):
        self.marca_motor=marca_motor
        self.tipo_motor=tipo_motor
        self.potencia=potencia

    def criar_motor(self):
        if self.tipo_motor=="Eletrico":
            return Motor_Eletrico(self.marca_motor,self.tipo_motor,self.potencia)
        if self.tipo_motor=="Combustão":
            return Motor_Cobustao(self.marca_motor,self.tipo_motor,self.potencia)
        if self.tipo_motor=="Hibrido":
            return Motor_Hibrido(self.marca_motor,self.tipo_motor,self.potencia)


class Motor:
    """Classe Motor"""
    def __init__(self,marca,potencia):
        self.marca=marca
        self.potencia=potencia


class Motor_Eletrico(Motor):
    """Classe Motor Eletrico-> Herda de Motor"""
    def __init__(self, marca,tipo_motor,potencia):
        super().__init__(marca,potencia)
        self.tipo_motor=tipo_motor


class Motor_Cobustao(Motor):
    """Classe Motor Combusão-> Herda de Motor"""
    def __init__(self, marca,tipo_motor,potencia):
        super().__init__(marca,potencia)
        self.tipo_motor=tipo_motor


class Motor_Hibrido(Motor):
    """Classe Motor Hibrido-> Herda de Motor"""
    def __init__(self, marca,tipo_motor,potencia):
        super().__init__(marca,potencia)
        self.tipo_motor=tipo_motor


class Caminhao(Veiculos):
    """Classe Motor Caminhão-> Herda de Veiculo"""
    def __init__(self, dono,tipo_veiculo, marca_veiculo, marca_motor, tipo_motor, potencia):
        super().__init__(dono, marca_veiculo, marca_motor, tipo_motor, potencia)
        self.tipo_veiculo=tipo_veiculo

    def printar_veiculo(self):
        print(f"Dono: {self.dono}")
        print(f"Tipo: {self.tipo_veiculo}")
        print(f"Marca do Veiculo: {self.marca_veiculo}")
        print(f"Marca do Motor: {self.motor.marca}")
        print(f"Tipo do Motor: {self.motor.tipo_motor}")
        print(f"Potencia: {self.motor.potencia}")


class Carro(Veiculos):
    """Classe Motor Caminhão-> Herda de Veiculo"""
    def __init__(self, dono,tipo_veiculo, marca_veiculo, marca_motor, tipo_motor, potencia):
        super().__init__(dono, marca_veiculo, marca_motor, tipo_motor, potencia)
        self.tipo_veiculo=tipo_veiculo

    def printar_veiculo(self):
        print(f"Dono: {self.dono}")
        print(f"Tipo: {self.tipo_veiculo}")
        print(f"Marca do Veiculo: {self.marca_veiculo}")
        print(f"Marca do Motor: {self.motor.marca}")
        print(f"Tipo do Motor: {self.motor.tipo_motor}")
        print(f"Potencia: {self.motor.potencia}")


class Moto(Veiculos):
    """Classe Motor Caminhão-> Herda de Veiculo"""
    def __init__(self, dono,tipo_veiculo, marca_veiculo, marca_motor, tipo_motor, potencia):
        super().__init__(dono, marca_veiculo, marca_motor, tipo_motor, potencia)
        self.tipo_veiculo=tipo_veiculo
    
    def printar_veiculo(self):
        print(f"Dono: {self.dono}")
        print(f"Tipo: {self.tipo_veiculo}")
        print(f"Marca do Veiculo: {self.marca_veiculo}")
        print(f"Marca do Motor: {self.motor.marca}")
        print(f"Tipo do Motor: {self.motor.tipo_motor}")
        print(f"Potencia: {self.motor.potencia}")

Carro1=Veiculo_Factory("Gabriel","Carro","Ferrari","GM","Combustão","100cv").criar_veiculo()
Carro1.printar_veiculo()

print("-------------------------------------------------------")
Caminhao1=Veiculo_Factory("Felipe","Caminhão","Fiat","GM","Hibrido","100cv").criar_veiculo()
Caminhao1.printar_veiculo()

print("-------------------------------------------------------")
Moto1=Veiculo_Factory("Jorge","Moto","Suzuki","GM","Eletrico","80").criar_veiculo()
Moto1.printar_veiculo()