# programma chiede un numero e si deve disegnare un poligono di n lati con 2<n<11

from turtle import Turtle
t = Turtle()

n = int(input("numero di lati(2<n<11): "))
a = 180 - (n-2)*180/n
# a  = 360/n

t.forward(100)
t.left(a)
t.forward(100)
t.left(a)
t.forward(100)
t.left(a)
t.forward(100)
t.left(a)
t.forward(100)
t.left(a)
t.forward(100)
t.left(a)
t.forward(100)
t.left(a)
t.forward(100)
t.left(a)
t.forward(100)
t.left(a)
t.forward(100)
t.left(a)
t.forward(100)
t.left(a)

"""

i = 0

while i != n:
    t.forward(100)
    t.left(a)
    i = i + 1
"""

# t.forward(100)
# t.left(a)
# da ripetere n volte

x = input() # Metto un input per non far finire il programma