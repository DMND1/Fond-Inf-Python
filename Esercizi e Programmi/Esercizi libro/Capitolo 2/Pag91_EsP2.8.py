# Scrivere un programma che chieda all'utente le lunghezze dei lati di un rettangolo e visualizzi: 
# - L'area e il perimetro del rettangolo
# - La lunghezza della sua diagonale

from math import sqrt

x = float(input("Valore del lato n1: "))
y = float(input("Valore del lato n2: "))

area = x * y
p = 2*x + 2*y

diagonale = round(sqrt(x**2 + y**2), 1)

print("L'area del rettangolo vale:", area, "mentre il suo perimetro vale:", p, "e la sua diagonale:", diagonale)