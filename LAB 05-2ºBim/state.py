
from abc import abstractclassmethod


class Documment:
    """Classe documento"""
    def __init__(self,nome,estado_inicial):
        self.nome=nome
        self.state=estado_inicial

    @abstractclassmethod
    def render():
        pass
    @abstractclassmethod
    def publish():
        pass
    def change_state(self , next_state):
        #Função que muda de estado
        self.state=next_state
        self.state=State_Factory(self.nome,next_state).criar_estado()
        print(f"Estado Atual:{next_state}")


class State_Factory:
    """Fábrica do Estado"""
    def __init__(self,documento,estado):
        self.documento=documento
        self.estado=estado
    def criar_estado(self):
        if self.estado=="Draft":
            return Draft(self.documento)
        if self.estado=="Moderation":
            return Moderation(self.documento)
        if self.estado=="Published":
            return Published(self.documento)


class State:
    """Estado"""
    def render():
        pass
    def publish():
        pass


class Draft(State):
    """Estado Draft"""
    def __init__(self,documento):
        self.documento=documento

    def render(self):
        pass
    def publish_adm(self):
        return "Published"
    def publish_user(self):
        return "Moderation"


class Moderation(State):
    """Estado Moderation"""
    def __init__(self,documento):
        self.documento=documento

    def review_falied(self):
        return "Draft"
    def aproved_adm(self):
        return "Published"

class Published(State):
    """Estado Published"""
    def __init__(self,documento):
        self.documento=documento

    def expired(self):
        return "Draft"

#Casos testes

Doc=Documment("Documento1",Draft("Documento1"))

#Mudança de estados: Draft -> Published

Doc.change_state(Doc.state.publish_adm())

#Mudança de estados: Published -> Draft

Doc.change_state(Doc.state.expired())

#Mudança de estados: Draft -> Moderation

Doc.change_state(Doc.state.publish_user())

#Mudança de estados: Moderation -> Published

Doc.change_state(Doc.state.aproved_adm())