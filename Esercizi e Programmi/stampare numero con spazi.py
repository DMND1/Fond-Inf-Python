# scrivere un programma che legga un numero intero di 5 cifre
# tale numero lo deve stampare con uno spazio in mezzo a tutte le cifre

n = int(input("Numero: "))

n_str = str(n)

print(n_str[0], n_str[1], n_str[2], n_str[3], n_str[4])

# risolvere lo stesso esercizio senza passare per le stringhe

cifra1 = int(n/(10**4))
cifra2 = int(n//(10**3))-cifra1*10
cifra3 = int(n//(10**2))-cifra2*
cifra4 = int(n//(10**1))
cifra5 = int(n//(10**0))

print(cifra1, cifra2, cifra3, cifra4, cifra5)