# Scrivete le seguenti funzioni e progettate un programma che le collaudi:
# - def smallest(x, y, z)   # restituisce l'argomento minore
# - def average(x, y, z)    # restituisce la media

def smallest(x, y, z):
    return(min(x, y, z))

def average(x, y, z):
    somma = x + y + z
    return(somma / 3)

n1 = float(input("Primo numero: "))
n2 = float(input("Secondo numero: "))
n3 = float(input("Terzo numero: "))

print(smallest(n1, n2, n3))
print(average(n1, n2, n3))