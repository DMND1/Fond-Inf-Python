# far partire 3 o 4 tartarughe da una linea di partenza, vedere chi arriva per prima alla righa di fine
# per ogni tartaruga generare un numero che equivale al numero di pixel che deve avanzare

# Pseudo codice:
# from random import randint (in alternatiava va bene anche scrivere: import random; in questo caso però "randint" va sostituito con "random.randint")
# from turtle import Turtle (o in alternativa: import turtle as t)

# t = Turtle()

# disegna linea di arrivo

# t_1 = Turtle()
# t_2 = Turtle()
# t_3 = Turtle()

# disegna linea di partenza
# muovere le tartarughe in posizione

# Fine = False
# while Fine != True: (Mentre Fine è Falso)
#   t_1.forward(randint(50,100))
#   t_2.forward(randint(50,100))
#   t_3.forward(randint(50,100))
#   if t_1.xcor() == 500 or t_2.xcor() == 500 or t_3.xcor() == 500:
#       Fine = True

from random import randint
from turtle import Turtle

# Disegna linea di arrivo
t = Turtle()
t.penup()
t.forward(500)
t.pendown()
t.left(90)
t.forward(50)
t.right(180)
t.forward(100)
t.hideturtle()

# Tartarughe in competizione
t_1 = Turtle()
t_2 = Turtle()
t_3 = Turtle()

# Posizionamento tartaruga 1
t_1.right(90)
t_1.forward(50)
t_1.left(90)
# Posizionamento tartaruga 2
t_3.left(90)
t_3.forward(50)
t_3.right(90)
# Posizionamento tartaruga 3
t_1.penup()
t_2.penup()
t_3.penup()

# Ciclo
Fine = False
while Fine != True:
    # Definisco la massima distanza percorribile, oltre la quale le tartartughe andrebbero oltre la linea di fine
    massima_distanza_t_1 = 500 - t_1.xcor()
    massima_distanza_t_2 = 500 - t_2.xcor()
    massima_distanza_t_3 = 500 - t_3.xcor()
    # Movimento tartarughe
    t_1.forward(min(randint(1,10),massima_distanza_t_1))
    t_2.forward(min(randint(1,10),massima_distanza_t_2))
    t_3.forward(min(randint(1,10),massima_distanza_t_3))
    # Controllo se una tartaruga è arrivata alla fine
    if t_1.xcor() == 500 or t_2.xcor() == 500 or t_3.xcor() == 500:
       Fine = True

# in alternativa: (anche se in questo modo la tartaruga t_1 ha la "precedenza", cioè viene controllata coma vincitrice per prima rispetto alle altre)
"""
    # Controllo se una tartaruga è arrivata alla fine e stampo quale è arrivata per prima
    if t_1.xcor() == 500:
        Fine = True
        print("La tartaruga n°1 ha vinto")
    elif t_2.xcor() == 500:
        Fine = True
        print("La tartaruga n°2 ha vinto")
    elif t_3.xcor() == 500:
        Fine = True
        print("La tartaruga n°3 ha vinto")
"""

x = input() # Metto un input per non far finire il programma