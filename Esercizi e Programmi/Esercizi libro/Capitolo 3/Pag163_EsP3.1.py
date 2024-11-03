# Scrivete un programma che acquisisca un numero intero e visualizi un messaggio diverso nei casi in cui sia negativo, uguale a zero o positivo

# Pseudocodice:
# leggi n
# se n è negativo:
#   stampa n è negativo
# altrimenti se n è uguale a zero: 
#   stampa n è uguale a zero
# altrimenti se n è positivo:
#   stampa n è positivo

n = int(input("Numero intero: "))

if n < 0:
    risultato = "n è negativo"
elif n == 0:
    risultato = "n è uguale a zero"
else:   # ossia se n è positivo:
    risultato = "n è positivo"

print(risultato)