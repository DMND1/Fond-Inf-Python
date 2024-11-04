# programma chiede un numero e si deve disegnare un poligono di n lati con 2<n<11

from turtle import Turtle
t = Turtle()

n = int(input("numero di lati(2<n<11): "))
angolo = 180 - (n-2)*180/n
# a  = 360/n

t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.forward(100)
t.left(angolo)
t.hideturtle()

x = input() # Metto un input per non far finire il programma