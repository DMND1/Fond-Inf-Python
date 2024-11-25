# Realizzare una funzione che ricevendo in ingresso due coordinate cartesiane le trasformi in polari

def ConvCoord(x, y):
    from math import sqrt, acos, pi
    ipotenusa = sqrt(x**2 + y**2)
    angolo = acos(x / ipotenusa)
    angolo = round((180 * angolo) / pi)
    return ipotenusa, angolo

print(ConvCoord(1,1))