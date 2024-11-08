# Scrivete programmi che leggano una sequenza di numeri interi e visualizzino quanto segue: 
# - il valore minimo e il valore massimo tra quelli acquisiti
# - il numero di valori pari e il numero di valori dispari tra quelli acquisiti
# - le somme parziali di tutti i numeri acquisiti, calcolate e visualizzate dopo ogni acquisizione 
#   (se, ad esempio, i valori in ingresso sono 1 7 2 9, il programma deve visualizzare 1 8 10 19)
# - i valori adiacenti duplicati (se ad esempio, i valori acquisiti sono 1 3 3 4 5 5 6 6 6 3, il programma deve visualizzare 3 5 6)

# Il valore minimo e il valore massimo tra quelli acquisiti
n = input("Inserire un numero: ")

minimo = int(n)
massimo = int(n)

while n != "":
    n = int(n)
    if n < minimo:
        minimo = n
    elif n > massimo:
        massimo = n
    n = input("Inserire un numero: ")

print("Il valore massimo è:", massimo, "e il valore minimo è:", minimo)


# Il numero di valori pari e il numero di valori dispari tra quelli acquisiti
n = input("Inserire un numero: ")

pari = 0
dispari = 0

while n != "":
    n = int(n)
    if n % 2 == 0:
        pari += 1
    elif n % 2 != 0:
        dispari += 1
    n = input("Inserire un numero: ")

print("I numeri dispari sono:", dispari, "e i numeri pari sono:", pari)


# Le somme parziali di tutti i numeri acquisiti, calcolate e visualizzate dopo ogni acquisizione
n = input("Inserire un numero: ")

somma = 0

while n != "":
    n = int(n)
    somma += n
    print(somma)
    n = input("Inserire un numero: ")


# I valori adiacenti duplicati (se ad esempio, i valori acquisiti sono 1 3 3 4 5 5 6 6 6 3, il programma deve visualizzare 3 5 6)
previous = int(input("Inserire un numero: "))
n = int(input("Inserire un numero: "))

risultato = "Non ci sono valori adiacenti duplicati"

while n != "":
    n = int(n)
    if previous == n and not(str(n) in risultato):
        risultato = risultato.replace("Non ci sono valori adiacenti duplicati","")
        risultato += str(n) + " "
    previous = n
    n = input("Inserire un numero (lasicare vuoto per terminare): ")

print(risultato)