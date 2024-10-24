# Esercizio a pag 50 del libro: dobbiamo calcolare il tempo totale necessario al robot per raggiungere il proprio obiettivo, sulla basedei seguenti dati ...

""" 
T1 e T2 sono i due tempi che servono per percorrere rispettivamente i tratti L1 e L2

S1=L1/T1
S2=L2/T2
Calcola T1 che vale T1=L1/S1
    Per calcolare T2 dobbiamo calcolare prima L2
    L2=sqrt((dx-L1)^2 + (dy)^2)     (scritto in formula non in codice)
Calcola T2 che vale T2=L2/S2
Stampa T1 + T2
"""

# Il programma deve chiedere all'utente tutti i dati, poi svolegere i calcoli e stampare il risultato
# Programma di ottimizzazione per cercare il tempo minimo possibile per arrivare alla destinazione

from math import *

dx = float(input("Distanza tra il robot e l'oggetto in direzione x: "))
dy = float(input("Distanza tra il robot e l'oggetto in direzione y: "))
s1 = float(input("velocità del robot sulla strada: "))
s2 = float(input("velocità del robot sul terreno roccioso: "))
l1 = float(input("lunghezza del primo traddo dello spostamento: "))

t1 = l1 / s1

l2 = sqrt((dx-l1)**2 + dy**2)

t2 = l2/s2

print("Il tempo totale che serve al robot per arrivare all'oggetto è:", t1 + t2)