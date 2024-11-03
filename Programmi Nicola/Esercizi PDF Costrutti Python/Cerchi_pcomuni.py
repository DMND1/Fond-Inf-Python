#Date le coordinate dei centri e i raggi di due circonferenze, stabilire se hanno punti in comune
from math import sqrt

#faccio inserire i dati relativi ai cerchi e calcolo successivamente la distanza fra i centri

cx1 = int(input(" inserci l'ascissa del centro del primo cerchio: "))
cy1 = int(input("Inserisci l'ordinata del centro del primo cerchio: "))
r1 = float(input("inserisci il raggio del primo cerchio: "))

cx2 = int(input(" inserci l'ascissa del centro del secondo cerchio: "))
cy2 = int(input("Inserisci l'ordinata del centro del secondo cerchio: "))
r2 = float(input("inserisci il raggio del secondo cerchio: "))

d = sqrt(pow(cx2-cx1,2)+pow(cy2-cy1,2))

if d > r1 + r2:
    print("I cerchi non hanno punti in comune")
elif d == r1 + r2:
    print("I cerchi hanno un solo punto in comune")
elif abs(r1 - r2) < d < r1 + r2:
    print("I due cerchi hanno due punti in comune")

#funzionante