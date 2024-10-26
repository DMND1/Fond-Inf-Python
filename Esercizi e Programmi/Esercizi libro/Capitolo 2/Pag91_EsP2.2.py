# Scrivere un programma che visualizzi il perimetro e la lunghezza della diagonale di un foglio di carta in formato "letter" (8.5 x 11 pollici, un pollice = 25,4 millimetri)

from math import *

pollice = 25.4                                          # 25.4 mm

larghezza = round(pollice * 8.5, 1)
altezza = pollice * 11

p = round(larghezza*2 + altezza*2, 1)

diagonale = round(sqrt(larghezza**2 + altezza**2), 1)

print("Il perimetro del foglio è:", p, "mm^2")
print("La diagonale del fogliuo è: ", diagonale, "mm")