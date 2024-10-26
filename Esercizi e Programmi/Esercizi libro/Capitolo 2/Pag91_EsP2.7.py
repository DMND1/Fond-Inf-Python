# Programma che chieda la lunghezza del raggio e visuallizzi:
# - L'area e la circonferenzna di un cerchio avente tale raggio
# - Il volume e l'area superficiale di una sfera evente tale raggio

from math import pi

r = float(input("Il raggio vale: "))

area = round(pi * r ** 2, 1)
circ = round(2 * pi * r, 1)

vol = round(4/3 * pi * r ** 3, 1)
area_sup = round(4 * area, 1)

print("L'area del cechio vale:", area, "e la sua circonferenza vale:", circ)
print("Il volume della sfera vale:", vol, "e l'area della sua superficie vale:", area_sup)