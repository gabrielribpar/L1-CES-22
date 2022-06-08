from abc import abstractclassmethod
from numpy import append
from tkinter import *

from setuptools import Command
class Banco:
    """Classe Banco"""
    def __init__(self):
        self.clientes=[]
    
    def cadastrar_cliente(self,cliente):
        self.clientes.append(cliente)

    def verificar_saldo(self,codigo):
        for cliente in self.clientes:
            if cliente.codigo==codigo:
                saida["text"]=f"Saldo de {cliente.saldo}"
                break

    def sacar(self,codigo,valor):
        texto=0
        for cliente in self.clientes:
            if cliente.codigo==codigo:
                if valor<cliente.saldo:
                    cliente.saldo=cliente.saldo-valor
                    texto=f"Foi sacado {valor}"
                else:
                    texto=f"Saldo Insuficiente"
                    break
        saida["text"]=texto

    def deposito(self,codigo,valor):
        for cliente in self.clientes:
            if cliente.codigo==codigo:
                cliente.saldo=cliente.saldo+valor
                saida["text"]=f"Foi depositado {valor}"
                break

    def transferencia(self,codigo1,codigo2,valor):
        cliente1=0
        cliente2=0
        for cliente in self.clientes:
            if cliente.codigo==codigo1:
                cliente1=cliente
        for cliente in self.clientes:
            if cliente.codigo==codigo2:
                cliente2=cliente
        
        if valor<cliente1.saldo:
            cliente1.saldo=cliente1.saldo-valor
            cliente2.saldo=cliente2.saldo+valor
            saida["text"]=f"Foi transferido {valor} de {cliente1.nome} para {cliente2.nome}"
        else:
            saida["text"]("Saldo Insuficiente")

class Pessoa:
    """Classe Pessoa"""
    def __init__(self,nome,cpf,identidade):
        self.nome=nome
        self.cpf=cpf
        self.identidade=identidade


class Cliente_Banco(Pessoa):
    """Classe Cliente do Banco"""
    def __init__(self, nome, cpf, identidade,codigo,saldo):
        super().__init__(nome, cpf, identidade)
        self.saldo=saldo
        self.codigo=codigo

class Comando:
    """Classe de comando"""
    @abstractclassmethod
    def execute(self):
        pass

class Comando_Saldo(Comando):
    """Classe do comando verificar saldo"""
    def __init__(self,banco):
        self.banco=banco
    def execute(self):
        banco.verificar_saldo("01")

class Comando_Sacar(Comando):
    """Classe do comando sacar"""
    def __init__(self,banco,valor):
        self.banco=banco
        self.valor=valor
    def execute(self):
        banco.sacar("01",int(self.valor))

class Comando_Deposito(Comando):
    """Classe do comando deposito"""
    def __init__(self,banco,valor):
        self.banco=banco
        self.valor=valor
    def execute(self):
        banco.deposito("01",int(self.valor))

class Comando_Transferencia(Comando):
    """Classe do comando transferencia"""
    def __init__(self,banco,codigo1,codigo2,valor):
        self.banco=banco
        self.codigo1=codigo1
        self.codigo2=codigo2
        self.valor=valor
    def execute(self):
        banco.transferencia("01","02",int(self.valor))

class Invoke:
    """Classe que invoca os comandos"""
    def __init__(self,banco,En1) -> None:
        self.banco=banco
        self.En1=En1
    def invoke_sacar(self):
        Comando_Sacar(self.banco,self.En1.get()).execute()
    def invoke_deposito(self):
        Comando_Deposito(self.banco,self.En1.get()).execute()
    def invoke_transferencia(self):
        Comando_Transferencia(self.banco,"01","02",self.En1.get()).execute()
    def invoke_saldo(self):
        Comando_Saldo(banco).execute()



cl=Cliente_Banco("Gabriel","152246842-82","2569475","01",1000)
cl2=Cliente_Banco("João","152356842-82","2523475","02",580)
banco=Banco()
banco.cadastrar_cliente(cl)
banco.cadastrar_cliente(cl2)



#Inicializar janela
janela=Tk()
janela.title("Banco")
janela.geometry("490x560+610+153")

#Importar imagens
img=PhotoImage(file="Banco_Flexão.png")
img2=PhotoImage(file="B_Sacar.png")
img3=PhotoImage(file="B_Deposito.png")
img4=PhotoImage(file="B_Trans.png")
img5=PhotoImage(file="B_Saldo.png")
lab=Label(janela, image=img)
lab.pack()

# Criando Entradas
En1=Entry(janela,bd=2, font=("Calibri",15),justify=CENTER)
En1.place(width=335 , height= 45, x=80, y=180)
valor=En1.get()
#Criação Botoes
bt_sacar=Button(janela, bd=0,image=img2,command=Invoke(banco,En1).invoke_sacar)
bt_sacar.place(width=95 , height= 45, x=30, y=260)
bt_deposito=Button(janela, bd=0,image=img3,command=Invoke(banco,En1).invoke_deposito)
bt_deposito.place(width=140 , height= 45, x=150, y=260)
bt_transferencia=Button(janela, bd=0,image=img4,command=Invoke(banco,En1).invoke_transferencia)
bt_transferencia.place(width=150 , height= 45, x=320, y=260)
bt_saldo=Button(janela, bd=0,image=img5,command=Invoke(banco,En1).invoke_saldo)
bt_saldo.place(width=130 , height= 40, x=180, y=347)

#Criar texto saida
saida=Label(janela, text="")
saida.place(width=335 , height= 45, x=80, y=450)
janela.mainloop()

