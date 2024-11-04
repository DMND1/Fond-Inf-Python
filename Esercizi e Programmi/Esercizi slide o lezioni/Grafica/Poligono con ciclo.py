from turtle import Turtle
t = Turtle()

n = int(input("numero di lati: "))
a  = 360 / n
# a = 180 - (n-2) * 180 / n

# t.forward(100)
# t.left(a)
# da ripetere n volte

# Con for:

for i in range(0,n):
    t.forward(1000/n)   # 1000/n per fare entrare le figura nella finestra comunque si scelga n
    t.left(a)

# Per colorarlo:

t.begin_fill()

for i in range(0,n):
    t.forward(1000/n)   # 1000/n per fare entrare le figura nella finestra comunque si scelga n
    t.left(a)

t.end_fill()

# Con while:
i = 0

while i != n:
    t.forward(1000/n)   # 1000/n per fare entrare le figura nella finestra comunque si scelga n
    t.left(a)
    i = i + 1

x = input() # Metto un input per non far finire il programma
