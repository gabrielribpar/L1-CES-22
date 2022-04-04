

def decorador(funcao): 
    """Função decoradora"""
    def interna(civil,*args,**kwargs):
        """Insere o estado civil da pessoa"""
        retultado=funcao(*args,**kwargs)
        print(f'Estado Civil:{civil}')
        return funcao
    return interna

@decorador
def imprime_Dados(id,nome,cpf):
    """Função decorada:Imprime os dados de uma pessoa"""
    print('---------Dados------------\n')
    print(f'Nome:{nome}')
    print(f'CPF:{cpf}')
    print(f'Id:{id}')

imprime_Dados(civil='Solteiro',id=123456, nome='Rogério', cpf=123456789)