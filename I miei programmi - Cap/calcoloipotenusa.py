#programma che dati 2 cateti calcoli l'ipotenusa arrotondata fino a 10e-5

from math import sqrt

c1 = float(input("Inserire lunghezza C1: "))
c2 = float(input("Inserire lunghezza C2: "))

a = sqrt(c1*c1+c2*c2)
print("La lunghezza dell'ipotenusa è: ", round(a, 5))

