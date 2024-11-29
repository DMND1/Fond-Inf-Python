from math import sqrt,atan2,degrees
def convpolare(x,y):
    r = sqrt(x**2+y**2) #calcola il raggio 
    angolo = atan2(y, x) #Calcola l'angolo della coordinata polare
    return r, degrees(angolo) #faccio restituire il raggio e l'angolo in gradi

#main program

x = float(input("Inserisci l'ascissa: "))
y = float(input("Inserisci l'ordinata: "))

print(convpolare(x,y))