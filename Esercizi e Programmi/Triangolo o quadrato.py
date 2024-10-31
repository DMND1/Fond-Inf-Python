# Con turtle se n = 3 fare un triangolo altrimenti fare un quadrato

from turtle import Turtle
t = Turtle()

n = int(input("Il numero scelto è: "))

if n == 3 :
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
else :
   t.forward(100)
   t.left(90)
   t.forward(100)
   t.left(90)
   t.forward(100)
   t.left(90)
   t.forward(100)
   t.left(90)

t.hideturtle()

x = input() # Metto un input per non far finire il programma