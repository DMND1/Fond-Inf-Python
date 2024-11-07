# Scrivere un programma che simuli mille lanci di due dadi e che altermine stampi il numero delle volte che è uscita una coppia di valori uguali

# Pseudocodice:
# import random
# risultato = 0
# Fai mille lanci di 2 dadi
# Se la faccia dei due dadi all'n-esimo lancio coincide aumenta di 1 il risultato
# altrimenti pass

import random

risultato = 0

"""
for i in range(1,1001) :
    if random.randint(1,6) == random.randint(1,6):
        risultato = risultato + 1
"""

# Per rendere il programma più comprensibile si potrebbe scrivere:

for i in range(1000) :    # Che è analogo a for i in range(0,1000)
    faccia_dado1 = random.randint(1,6)
    faccia_dado2 = random.randint(1,6)
    if faccia_dado1 == faccia_dado2 :
        risultato = risultato + 1

print("Il numero di volte che è uscita la stessa faccia è:", risultato)