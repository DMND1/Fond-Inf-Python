from turtle import Turtle
t = Turtle()

t.forward(100) # Avanza di 100 pixel
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.hideturtle()
t.showturtle()

t.right(90)

t.up()
t.forward(100)
t.down()

t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

t.hideturtle()

t.showturtle()
t.up()
t.right(90)
t.forward(100)

t.pensize(7)
t.down()
t.forward(100)
t.right(90)
t.pencolor("red")
t.forward(100)

t.begin_fill()
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

t.up()
t.back(300)
t.down()
t.pensize(2)
t.circle(50)

x = input()