# Realizzare un programma che, chieste le coordinate dei centri e i raggi di due cerchi, controlli se i due cerchi hanno punti in comune

# Pseudocodice:
# from math import sqrt
# leggi x1 e y1 (coordinate) del centro 1
# leggi r1
# leggi x2 e y2 (coordinate) del centro 2
# leggi r2
# calcola la distanza tra i due centri = distanza_C1C2
# calcola la somma dei due raggi = somma_r1r2
# se i due centri non coincidono:
#   se distanza_C1C2 > somma_r1r2
#       stampa: I due cerchi non hanno punti in comune
#   se distanza_C1C2 < somma_r1r2
#       stampa: I due cerchi hanno due punti in comune
#   se distanza_C1C2 == somma_r1r2
#       stampa: I due cerchi sono tangeni, hanno un punto in comune (con molteplicità doppia)
# se i due centri coincidono e i raggi sono diversi:
#   stampa: I due cerchi non hanno punti in comune
# se i due centri coincidono e i raggi (non nulli) anche:
#   stampa: I due cerchi hanno infiniti punti in comune
# se i due centri coincidono e i raggi (nulli) anche:
#   stampa: Le due circonferenze (degeneri) hanno un solo punto in comune

from math import sqrt

x1 = float(input("Ascissa centro 1: "))
y1 = float(input("Ordinata centro 1: "))
r1 = float(input("Raggio primo cerchio: "))

x2 = float(input("Ascissa centro 2: "))
y2 = float(input("Ordinata centro 2: "))
r2 = float(input("Raggio secondo cerchio: "))

distanza_C1C2 = sqrt((x1-x2)**2 + (y1-y2)**2)
somma_r1r2 = r1 + r2
# La sommma di r1 e r2 potrebbe non essere esattamente 0, per cui poniamo e con un numero di cifre dopo la virgola deciso in modo arbitrario:
e = 0.000000000001


if distanza_C1C2 > somma_r1r2 :
    risultato = "I due cerchi non hanno punti in comune"
elif distanza_C1C2 < somma_r1r2 :
    risultato = "I due cerchi hanno punti in comune"
elif abs(distanza_C1C2 - somma_r1r2)<e:   # ossia se distanza_C1C2 == somma_r1r2
    risultato = "I due cerchi sono tangeni, hanno un punto in comune (con molteplicità doppia)"

"""
# Programma del professore:
if distanza_C1C2 > somma_r1r2 :
    risultato = "I due cerchi non hanno punti in comune"
else:
    if abs(distanza_C1C2 - somma_r1r2)<e:   # ossia se distanza_C1C2 == somma_r1r2
        risultato = "I due cerchi sono tangeni, hanno un punto in comune (con molteplicità doppia)"
    else:                                   # ossia se distanza_C1C2 < somma_r1r2
        risultato = "I due cerchi hanno punti in comune"
"""

print(risultato)