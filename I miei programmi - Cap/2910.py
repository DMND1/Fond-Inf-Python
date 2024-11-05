from turtle import Turtle
from math import tan, pi

t = Turtle()
x = int(input("Inserisci numero di poligoni da generare: "))
n = int(input("Inserisci il numero di lati del poligono: "))
h = int(input("Inserisci l'altezza del poligono: "))
color = str(input("Inserisci il colore del poligono: "))

l=0
t.fillcolor(color)
t.begin_fill()
for _ in range(x):
    t.up()
    t.forward(h/2)
    t.down()
    l = float(h*(2*tan(pi/n)))
    for _ in range(n):
        t.forward(l)
        t.left(360/n)
t.end_fill()


