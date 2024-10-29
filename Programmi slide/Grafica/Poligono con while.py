from turtle import Turtle
t = Turtle()

n = int(input("numero di lati: "))
a = 180 - (n-2)*180/n
# a  = 360/n


# t.forward(100)
# t.left(a)
# da ripetere n volte

i = 0

while i != n:
    t.forward(1000/n)   # 1000/n per fare entrare le figura nella finestra comunque si scelga n
    t.left(a)
    i = i + 1

# Per colorarlo:

i = 0

t.begin_fill()

while i != n:
    t.forward(1000/n)   # 1000/n per fare entrare le figura nella finestra comunque si scelga n
    t.left(a)
    i = i + 1

t.end_fill()

x = input() # Metto un input per non far finire il programma