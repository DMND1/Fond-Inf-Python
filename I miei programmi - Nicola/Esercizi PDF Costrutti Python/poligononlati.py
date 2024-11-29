from turtle import Turtle

n = int(input("Inserisci i lati del poligono da disegnare: "))

angolo = 360/n
t = Turtle()
for i in range (n):
    t.forward(100)
    t.left(angolo)

