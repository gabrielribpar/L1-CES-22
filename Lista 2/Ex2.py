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
    #Fica chamando a função em um tempo determinado
    turtle.ontimer(advance_state_machine, t=500) 
    

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

advance_state_machine() #Inicia as chamadas


wn.listen() # Listen for events
wn.mainloop()