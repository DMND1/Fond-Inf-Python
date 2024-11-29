##Pong

from turtle import *
from math import *
from datetime import *
from calendar import *

box = Turtle()
pallina = Turtle()
r1 = Turtle()
r2 = Turtle()

#Coordinate box
boxX = 600
boxY = 400

#Disegno box
box.hideturtle()
box.speed(100)
box.up()
box.goto(-boxX / 2, boxY / 2)
box.down()
box.pensize(2)
box.fd(boxX)
box.right(90)
box.fd(boxY)
box.right(90)
box.fd(boxX)
box.right(90)
box.fd(boxY)
box.right(90)
scritta = Turtle()
scritta.hideturtle()
scritta.up()
scritta.goto(-boxX / 2 + 10, boxY / 2 + 10)
scritta.down()
if day_name[date.today().weekday()] == "Tuesday" :
    scritta.write("OGGI SIETE TANTI A LEZIONE", font = ("Arial", 30, "normal"))

#Inizio racchette
r1.up()
r1.speed(100)
r1.goto(-boxX / 2, boxY / 2)
r1.shape("square")

#Inizio racchette
r2.up()
r2.speed(100)
r2.goto(boxX / 2, boxY / 2)
r2.shape("square")

#Posizione iniziale pallina
pallina.hideturtle()
pallina.up()
pallina.goto(-boxX / 2, boxY / 2)
pallina.showturtle()
pallina.shape("circle")
pallina.turtlesize(0.5, 0.5, 0.5)

#Movimento pallina
angoloPallina = 30
PASSO = 10
pallina.right(angoloPallina)
pallina.fd(PASSO)
pallina.speed(100)
girato = False

while True :
    if girato == False :
        if pallina.ycor() < boxY / 2 and pallina.ycor() > -boxY / 2 :
            pallina.fd(PASSO)
        else :
            pallina.left(2 * angoloPallina) if pallina.ycor() < 0 else pallina.right(2 * angoloPallina)
            pallina.fd(PASSO)

    if girato == True :
        if pallina.ycor() < boxY / 2 and pallina.ycor() > -boxY / 2 :
            pallina.fd(PASSO)
        else :
            pallina.right(2 * angoloPallina) if pallina.ycor() < 0 else pallina.left(2 * angoloPallina)
            pallina.fd(PASSO)

    #Movimento racchette
    if girato == False :
        r2.goto(boxX / 2, pallina.ycor())

    if girato == True :
        r1.goto(-boxX / 2, pallina.ycor())

    #Rimbalzo racchette   
    if pallina.xcor() <= -boxX / 2 :
        saleScende = -1 if pallina.heading() < 180 else 1
        pallina.setheading(-angoloPallina * saleScende)
        girato = False
    
    if pallina.xcor() >= boxX / 2 :
        saleScende = -1 if pallina.heading() < 180 else 1
        pallina.setheading(180 + angoloPallina * saleScende)
        girato = True