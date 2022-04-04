from abc import abstractmethod

class Pessoa:

    
    """Classe Pessoa"""
    def __init__(self,nome,id,idade,saldo_conta):
        """Construtor"""
        self.nome=nome
        self.id=id
        self.idade=idade
        self.saldo_conta=saldo_conta


    def ano_Nascimento(self): 
        """Método de Instancia:"""
        """Cada pessoa tem seu ano de nascimento"""
        return 2022-self.idade


    @classmethod
    def por_ano_nascimento(cls,nome,id,ano_nascimento,saldo_conta):
        """Método de classe: Toda classe tem e não depende da instancia"""
        """Caso queira criar uma instancia pelo ano de nascimento e nao idade"""
        return cls(nome,id,2022-ano_nascimento,saldo_conta)


    @staticmethod
    def calular_Salario(horas_trabalhadas, valor_por_hora):
        "Método Estático:"
        "Caso queiramos calcular o salario, sem instanciar um objeto"
        return horas_trabalhadas*valor_por_hora


    @abstractmethod
    def receber_Salario(self):
        """Método Abstrato:"""
        """Nas classes filhas(Ex:Garçom) esse metodo sera usado"""
        pass

    
class Garçom(Pessoa):
    salario=1000
    
    def __init__(self, nome, id, idade,saldo_conta,empresa):
        """Construtor"""
        super().__init__(nome,id,idade,saldo_conta)
        self.empresa=empresa


    def receber_Salario(self):
        """Para cada classe filha esse método se comporta diferente"""
        self.saldo_conta=self.saldo_conta+self.salario


"""###############TESTANDO################"""

if __name__== '__main__':
    #Criando a pessoa 1
    P1=Pessoa('Joao',123456789,25,1000) 
    #Usando o método de instancia
    print(f"Ano de Nascimento:{P1.ano_Nascimento()}") 
    #Usando método de classe
    P2=Pessoa.por_ano_nascimento('Regina',123456789,1920,520) 
    #Usando método estático
    Salario_Pedreiro=Pessoa.calular_Salario(100,30)
    #Usando classe abstrata
    P3=Garçom('Flavia',123456789,29,2000,'Empresa')
    P3.receber_Salario()