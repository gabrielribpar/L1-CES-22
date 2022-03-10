import turtle

def desenhar_quadrado(t,sz):
    """ Faz a Tartaruga t desenhar um quadrado de tamanho sz"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

tela=turtle.Screen() # Inicializa a Tela
tela.bgcolor("lightgreen") #Coloca a cor de fundo
tela.title("Programa") # Coloca o Titulo da tela
tartaruga=turtle.Turtle() #Cria a Tartaruga
tartaruga.color("hotpink")
tartaruga.pensize(4)
for i in range(5):
    t_inicial=20+20*i #Define o tamanho dos quadrados
    desenhar_quadrado(tartaruga,t_inicial)
    tartaruga.penup() #Faz com que a tartaruga não desenhe ao se mover
    [x,y]=tartaruga.position() # Define a posição da tartaruga
    tartaruga.goto(x-10,y-10) #Move a tartaruga para a proxima posição
    tartaruga.pendown() #Retorna a caneta para que a tartaruga desenhe
tela.mainloop()  
