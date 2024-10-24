from math import *

a = float(input("Quanto vale il primo cateto? "))

b = float(input("Quanto vale il secondo cateto? "))

ipotenusa = sqrt(a*a + b*b)
print("L'ipotenusa vale:", ipotenusa)

# In alternativa si può anche scrivere:
print("L'ipotenusa vale:", sqrt(a*a + b*b))

# Oppure anche
print("L'ipotenusa vale: " + str(ipotenusa))