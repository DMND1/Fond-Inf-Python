# Scrivere una funzione che dati due cateti di un triangolo rettangolo calcoli l'ipotenusa
from math import sqrt

def ipotenusa(cateto1, cateto2):
    return sqrt(cateto1**2 + cateto2**2)