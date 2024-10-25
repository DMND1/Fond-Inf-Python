y = abs(-10)            # y vale 10
print(y)

y = round(7.526)        # y è l'intero più vicino, cioè 8
print(y)

y = round(7.526,2)      # il secondo argomento è il numero di cifre 
print(y)                # frazionarie desiderato. y vale 7.53

y = min(5, 2.1, 3, 7.4) # y vale 2.1
print(y)

y = max(-1.3, 7, 6.9)   # y vale 7 (intero)
print(y)

from math import pi, sqrt

raggio = 3
circonferenza = 2 * pi * raggio # circonferenza per cerchio di raggio 3
print(circonferenza)

lato = 4
diagonale = lato * sqrt(2)      # diagonale di un qudrato di lato 4 
print(diagonale)