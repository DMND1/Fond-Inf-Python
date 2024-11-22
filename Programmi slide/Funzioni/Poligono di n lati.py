from turtle import Turtle

LATO = 100

def poligono(lati):
    for i in range(0,lati):
        tarta.forward(LATO)
        tarta.left(360  / lati)

print(poligono(5))  # Stamperà: None    poiché la funizoine presa in considerazione è una procedura

n = int(input("Lati: "))

tarta = Turtle()
tarta.width(3)
tarta.color("red")

for i in range(0,n):
    poligono(n)
    tarta.left(360 / n)