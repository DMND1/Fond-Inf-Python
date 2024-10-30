# Il circuito di sintonizzazione rappresentato in figura è connesso a un'antenna e C è un valore di capacità variabile tra C_min e C_max. 
# Il circuito di sintonizzazione seleziona la frequenza f = 1 / (2 * pi * sqrt(L * C)) . Per poter progettare il circuito adatto a una determinata frequenza, 
# si calcola per prima cosa C = sqrt(C_min * C_max) , per poi calcolare l'induttanza L necessaria a partire dai valori di f e C. A questo punto il circuito
# può essere sintonizzato su qualsiasi frequenza appartenente all'intervallo delimitato da 
# f_min = 1 / (2 * pi * sqrt(L * C_max)) e da f_max = 1 / (2 * pi * sqrt(L * C_min))

# Scrivete un programma Python che aiuti a progettare il circuito di sintonizzanone per una specifica frequenza, usando un condensatore di capacità C variabile 
# tra C_min e C_max (valori di ingresso tipici potrebbero essere f = 16.7 MHz, C_min = 14 pF e C_max = 365 pF). Il programma deve acquisire, come dati in 
# ingresso, f (in Hz), C_min e C_max (in F), visualizzando il valore di induttanza richiesto e l'intervallo di frequenze sulle quali può essere sintonizzato 
# il circuito variando la capacità.

from math import pi, sqrt

f = float(input("La frequenza (in Hz) è: "))
C_min = float(input("La capacità minima (in F) è: "))
C_max = float(input("La capacità massima (in F) è: "))

C = sqrt(C_min * C_max)

L = 1 / ((2 * pi * f)**2 * C)

f_min = 1 / (2 * pi * sqrt(L * C_max))
f_max = 1 / (2 * pi * sqrt(L * C_min))

print("L'induttanza ha valore:", L, "H")
print("L'intervallo delle frequenze va da:", f_min, "Hz a", f_max, "Hz")