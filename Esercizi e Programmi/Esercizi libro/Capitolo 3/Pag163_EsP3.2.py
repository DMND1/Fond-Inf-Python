# Scrivete un programma che acquisisca un numero in virgola mobile e visualizzi il messaggio "zero" se è uguale a zero, altrimenti visualizi il messaggio "positive" (se è positivo)
# o "negative" (se è negativo). Aggiungete il messaggio "small" se il valore assoluto del numero è inferiore a 1 oppure "large" se è superiore a un milione

# Pseudocodice:
# leggi n
# risultato = ""
# se il valore assoluto di n è inferiore a 1:
#   risultato = "small "
# altrimenti se il valore assoluto di n è superiore a un milione:
#   risultato = "large "
# se n è negativo:
#   risultato = risultato + "negative"
# altrimenti se n è uguale a zero: 
#   risultato = "zero"
# altrimenti se n è positivo:
#   risultato = risultato + "positive"
# stampa il risultato

n = float(input("Numero intero: "))

risultato = ""

if abs(n) < 1 : 
    risultato = "small "
elif abs(n) > 1000000 :
    risultato = "large "
if n < 0:
    risultato = risultato + "negative"
elif n == 0:
    risultato = "zero"
else:   # ossia se n è positivo:
    risultato = risultato + "positive"

print(risultato)