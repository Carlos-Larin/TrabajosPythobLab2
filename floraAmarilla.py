import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("black")

# Creación de la tortuga
flor = turtle.Turtle()
flor.speed(10)

# Función para dibujar una cruz en la posición actual
def marcar_posicion():
    flor.penup()
    flor.goto(0, 0)  # Mover a la posición deseada, por defecto es el origen (0, 0)
    flor.pendown()
    flor.color("red")
    flor.write("X", align="center", font=("Arial", 16, "normal"))
    flor.penup()

# Función para dibujar un pétalo
def dibujar_petalo():
    flor.color("yellow")
    flor.begin_fill()
    flor.circle(60, 60)
    flor.left(120)
    flor.circle(60, 60)
    flor.left(120)
    flor.end_fill()

# Marcar la posición
marcar_posicion()

# Dibujar la flor completa
flor.goto(0, 0)
flor.pendown()
for _ in range(10):
    dibujar_petalo()
    flor.left(80)

# Dibujar el centro de la flor correctamente
flor.color("orange")
flor.penup()  # Levantar el lápiz para no dibujar mientras se mueve
flor.goto(20, -5)  # Mover al centro de la flor
flor.pendown()  # Bajar el lápiz para empezar a dibujar
flor.begin_fill()
flor.circle(20)  # Dibujar el círculo centrado
flor.end_fill()

# Función para dibujar el tallo
def dibujar_tallo():
    flor.color("green")
    flor.penup()
    flor.goto(10, -20)  # Comenzar desde el centro de la flor
    flor.right(175)  # Girar hacia abajo
    flor.pendown()
    flor.begin_fill()
    flor.forward(200)  # Dibujar el tallo
    flor.end_fill()

# Función para dibujar una hoja
def dibujar_hoja():
    flor.color("green")
    flor.begin_fill()
    flor.circle(40, 90)  # Dibujar media hoja
    flor.left(90)
    flor.circle(40, 90)  # Completar la hoja
    flor.end_fill()

# Dibujar el tallo
dibujar_tallo()

# Dibujar las hojas
flor.penup()
flor.goto(0, -100)  # Posición para la primera hoja
flor.left(45)  # Orientar hacia la izquierda
flor.pendown()
dibujar_hoja()

flor.penup()
flor.goto(0, -150)  # Posición para la segunda hoja
flor.right(90)  # Orientar hacia la derecha
flor.pendown()
dibujar_hoja()

# Ocultar la tortuga
flor.hideturtle()

# Mantener la ventana abierta
turtle.done()

"""
for _ in range(3):
    dibujar_petalo2()
    flor.left(80)

for _ in range(3):
    dibujar_petalo3()
    flor.left(80)


def dibujar_petalo2():
    flor.color("red")
    flor.begin_fill()
    flor.circle(60, 60)
    flor.left(120)
    flor.circle(60, 60)
    flor.left(120)
    flor.end_fill()

def dibujar_petalo3():
    flor.color("green")
    flor.begin_fill()
    flor.circle(60, 60)
    flor.left(120)
    flor.circle(60, 60)
    flor.left(120)
    flor.end_fill()
"""