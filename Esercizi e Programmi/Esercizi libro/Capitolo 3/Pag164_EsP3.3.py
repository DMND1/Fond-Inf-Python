# Scrivete un programma che legga un numero intero e visualizzi il numero delle sue cifre, verificando prima se il numero è >= 10, poi se è >= 100 e così via 
# (ipotizzando che tutti i possibili numeri interi siano inferiori a dieci miliardi). Se il numero è negativo, moltiplicatelo prima per -1.
# 
# Pseudocodice:
# leggi n
# risultato = 0
# se n >= 10:
#   risultato = risultato + 1
# se n >= 100:
#   risultato = risultato + 1
# ...
# se n >= 10000000000:
#   risultato = risultato + 1
# stampa il risultato

n = int(input("Numero intero: "))

if n < 0:
   n = -n

# In alternativa si potrebbe anche scrivere:
# n = abs(int(input("Numero intero: ")))

risultato = 1

if n >= 10:
   risultato = risultato + 1
if n >= 100:
   risultato = risultato + 1
if n >= 1000:
   risultato = risultato + 1
if n >= 10000:
   risultato = risultato + 1
if n >= 100000:
   risultato = risultato + 1
if n >= 1000000:
   risultato = risultato + 1
if n >= 10000000:
   risultato = risultato + 1
if n >= 100000000:
   risultato = risultato + 1
if n >= 1000000000:
   risultato = risultato + 1
if n >= 10000000000:
   risultato = risultato + 1

print("Il numero ha", str(risultato), "cifre")

# Ovviamente se non dobbiamo necessariamente usare gli if il programma si riduce a:

n = abs(int(input("Numero intero: ")))

n = str(n)

print("Il numero ha", str(len(n)), "cifre")