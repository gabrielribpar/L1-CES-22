import turtle


def draw_poly(t, n, sz):
    """ Função que desenha um polígono de n lados e tamanho sz """
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


tela = turtle.Screen()
tela=turtle.Screen() # Inicializa a Tela
tela.bgcolor("lightgreen") #Coloca a cor de fundo
tela.title("Programa") # Coloca o Titulo da tela
tess=turtle.Turtle() #Cria a Tartaruga
tess.color("hotpink")
tess.pensize(4)
draw_poly(tess, 8, 50) #Chamada da função
tela.mainloop() 