
import email
from random import randint
from tokenize import Token


class Livraria:
    def __init__(self,livros=[],clientes=[],outros_produtos=[],funcionarios=[],compra=[]):
        self.livros=[]
        self.outros_produtos=[]
        self.clientes=[]
        self.funcionarios=[]
        self.compras=[]

    def inserir_livro(self,livro):
        self.livros.append(livro)
        print(f"Livro {livro.titulo} Inserido")

    def alteracao_livro(self,versao_antiga,versao_nova):
        for i in range(len(self.livros)):
            if self.livros[i]==versao_antiga:
                self.livros[i]=versao_nova
        print(f"Livro {versao_antiga.titulo} foi alterado para {versao_nova.titulo}")
                
    def consulta_livro(self,autor):
        for i in range(len(self.livros)):
            if self.livros[i].autor==autor:
                print(self.livros[i].titulo)

    def remocao_livro(self,livro):
        for i in range(len(self.livros)):
            if self.livros[i]==livro:
                del(self.livros[i])
                print(f"Livro {livro.titulo} Removido")
                break

    def inserir_cliente(self,cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} Inserido")

    def alteracao_cliente(self,versao_antiga,versao_nova):
        for i in range(len(self.clientes)):
            if self.clientes[i]==versao_antiga:
                self.clientes[i]=versao_nova
                print(f"Cliente {versao_antiga.nome} foi alterado para {versao_nova.nome}")
                
    def consulta_cliente(self,cliente):
        for i in range(len(self.clientes)):
            if self.clientes[i]==cliente:
                self.clientes[i].print_cliente()


    def remocao_cliente(self,cliente):
        for i in range(len(self.clientes)):
            if self.clientes[i]==cliente:
                del(self.clientes[i])
                print(f"Cliente {cliente.nome} Removido")
                break
    
    def inserir_compra(self,compra):
        self.compras.append(compra)
        print(f"A compra {compra.codigo} Removido")

    def alteracao_compra(self,versao_antiga,versao_nova):
        for i in range(len(self.compras)):
            if self.compras[i]==versao_antiga:
                self.compras[i]=versao_nova
                print(f"A compra {versao_antiga.codigo} foi alterado para {versao_nova.codigo}")
                
    def consulta_compra(self,codigo):
        for i in range(len(self.compras)):
            if self.compras[i].codigo==codigo:
                self.compras[i].print_compra()

    def remocao_compra(self,compra):
        for i in range(len(self.compras)):
            if self.compras[i]==compra:
                del(self.compras[i])
                print(f"A compra {compra.codigo} Removido")
                break
    


class Produtos:
    def __init__(self,preco_venda,preco_compra):
        self.preco_venda=preco_venda
        self.preco_compra=preco_compra


class Livro(Produtos):
    def __init__(self,titulo,autor,genero,edicao,editora,preco_venda,preco_compra):
        super().__init__(preco_venda,preco_compra)
        self.autor=autor
        self.titulo=titulo
        self.genero=genero
        self.edicao=edicao
        self.editora=editora

class Pessoa:
    def __init__(self,nome,email):
        self.nome=nome
        self.email=email
    def print_pessoa(self):
        print(f"Nome:{self.nome}")
        print(f"Email:{self.email}")

class Autor(Pessoa):
    def __init__(self,nome,email,titulos_publicados):
        super().__init__(nome,email)
        self.titulos_publicados=titulos_publicados
    
    def print_autor(self):
        super().print_pessoa()
        print("Títulos Publicados:")
        for i in range(len(self.titulos_publicados)):
            print(f"-{self.titulos_publicados[i]}")


class Cliente(Pessoa):
    def __init__(self,nome,email,compras_passadas):
        super().__init__(nome,email)
        self.compras_passadas=compras_passadas
    
    def print_cliente(self):
        super().print_pessoa()
        print("Títulos Publicados(Código):")
        for i in range(len(self.compras_passadas)):
            print(f"- {self.compras_passadas[i].codigo}")

class Calculador_Imposto():
    def __init__(self):
        pass

class Compra:
    def __init__(self,produtos,quantidade,codigo):
        self.produtos=produtos
        self.quantidade=quantidade
        self.calculador_imposto=Calculador_Imposto()
        self.codigo=codigo

    def print_compra(self):
        print(f"Código:{self.codigo}")
        print("Livros:")
        for i in range(len(self.produtos)):
            print(f"{self.quantidade[i]}x {self.produtos[i].titulo}")

if __name__ == '__main__':
    Autor1=Autor('Token','nda','Senhor dos aneis')
    Autor2=Autor('J.K.Rowling','nda',['Harry Potter e a Pedra Filosofal','Harry Potter e a Ordem da Fenix'])
    Autor3=Autor('Scott Hahn','nda',['Todos os caminhos levam a Roma'])
    Autor4=Autor('Sun Tzu','nda',['A arte da guerra'])
    Livro1=Livro('Senhor dos aneis',Autor1,'Fantasia','3º','editora ITA',30,15)
    Livro2=Livro('Harry Potter e a Pedra Filosofal',Autor2,'Fantasia','1º','editora ITA',40,15)
    Livro3=Livro('Harry Potter e a Ordem da Fenix',Autor2,'Fantasia','5º','editora ITA',35,15)
    Livro4=Livro('Todos os caminhos levam a Roma',Autor3,'Biografia','2º','editora ITA',40,15)
    Livro5=Livro('A arte da guerra',Autor4,'Guerra','8º','editora ITA',30,15)
    Compra1=Compra([Livro1, Livro2],[1,3], 123)                                
    Compra2=Compra([Livro4, Livro3, Livro5],[2,1,1], 134)
    Compra3=Compra([Livro4, Livro5],[2,1], 256)
    Cliente1=Cliente('Gabriel','gabriel@gmail.com',[Compra1])
    Cliente2=Cliente('Vinicus','vinicus@gmail.com',[Compra2])
    Cliente3=Cliente('Joao','joao@gmail.com',[Compra3])
    Livraria1=Livraria()
    print("-----------INSERÇÃO LIVROS----------------")
    Livraria1.inserir_livro(Livro1)
    Livraria1.inserir_livro(Livro2)
    Livraria1.inserir_livro(Livro3)
    Livraria1.inserir_livro(Livro4)
    print("-----------INSERÇÃO CLIENTES--------------")
    Livraria1.inserir_cliente(Cliente1)
    Livraria1.inserir_cliente(Cliente2)
    print("-----------INSERÇÃO COMPRAS------------------")
    Livraria1.inserir_compra(Compra1)
    Livraria1.inserir_compra(Compra2)
    print("-----------CONSULTA AUTOR:Touken--------------")
    Livraria1.consulta_livro(Autor1)
    print("-----------Alteração Livro4->Livro5--------------")
    Livraria1.alteracao_livro(Livro4,Livro5)
    print("-----------Alteração Cliente2->Cliente3--------------")
    Livraria1.alteracao_cliente(Cliente2,Cliente3)
    print("-----------Alteração Cliente2->Cliente3--------------")
    Livraria1.alteracao_compra(Compra2,Compra3)
    print("-----------CONSULTA AUTOR:J.K.Rowling--------------")
    Livraria1.consulta_livro(Autor2)
    print("-----------REMOÇÃO COMPRA 1--------------")
    Livraria1.remocao_compra(Compra1)
    print("-----------REMOÇÃO Cliente 3--------------")
    Livraria1.remocao_cliente(Cliente3)
    print("-----------CONSULTA COMPRA 3--------------")
    Livraria1.consulta_compra(256)
    print("-----------CONSULTA Cliente 1--------------")
    Livraria1.consulta_cliente(Cliente1)

