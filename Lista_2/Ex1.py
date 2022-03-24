import turtle # Tess se torna um semáforo.


def draw_housing():
    """ Desenhe uma bela caixa para segurar os semáforos """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def advance_state_machine():
    """Cria uma máquina de estados"""
    global state_num
    if state_num == 0: # Transição do estado 0 para o estado 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transição do estado 1 para o estado 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transição do estado 2 para o estado 3
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0


def color_r():
    """Mude para Vermelho a Cor da Tartaruga"""
    tess.color("red")


def color_g():
    """Mude para Verde a Cor da Tartaruga"""
    tess.color("green")


def color_b():
    """Mude para Azul a Cor da Tartaruga"""
    tess.color("blue")


def increase_size():
    """Aumente o tamanho da caneta"""
    global size
    if size>0 and size<20:
        size=size+1
        tess.pensize(size)


def decrease_size():
    """Diminui o tamanho da caneta"""
    global size
    if size>1 and size<20:
        size=size-1
        tess.pensize(size)


def normal_shape():
    """Muda o formato para uma tartaruga"""
    tess.shape("turtle")


def square_shape():
    """Muda o formato para um   quadrado"""
    tess.shape("square")


def circle_shape():
    """Muda o formato para um   circulo"""
    tess.shape("circle")


def triangle_shape():
    """Muda o formato para um   triangulo"""
    tess.shape("triangle")


turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
draw_housing()
tess.penup()

# Posicione a tess no local onde a luz verde deve ser
tess.forward(40)
tess.left(90)
tess.forward(50)

# Transforme tess em um grande círculo verde
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

state_num = 0 # Variavel que guarda o estado da máquina
size=3 #Tamanho da caneta


wn.onkey(advance_state_machine, "space") #Ao pressionar espaco muda o estado da tartaruga
"""Modifica a cor da Tartaruga"""
wn.onkey(color_r, "R") 
wn.onkey(color_g, "G")
wn.onkey(color_b, "B")

"""Modifica o tamanho da caneta"""
wn.onkey(increase_size, "plus")
wn.onkey(decrease_size, "minus")

"""Modifica o formato da Tartaruga dependendo do número escolhido"""
wn.onkey(normal_shape, "0") #0-> Formato normal
wn.onkey(circle_shape, "1") #1-> Formato circulo
wn.onkey(square_shape, "2") #2-> Formato quadrado
wn.onkey(triangle_shape, "3") #3-> Formato triangulo

wn.listen() # Listen for events
wn.mainloop()