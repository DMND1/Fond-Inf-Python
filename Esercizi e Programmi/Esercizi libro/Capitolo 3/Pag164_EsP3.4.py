# Scrivete un programma che legga tre numeri e visualizzi il messaggio "all the same" se sono titti uguali, "all different" se sono tutti diversi e "neither" 
# se non sono tutti uguali e non sono tutti diversi

# Pseudocodice:
# leggi n1
# leggi n2
# leggi n3
# risultato = ""
# se n1 == n2 == n3:
#   risultato = "all the same"
# altrimenti se n1 != n2 and n1 !=n3 and n2 != n3:
#   risultato = "all different"
# altrimenti:
#   risultato = "neither"
# stampa il risultato

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

risultato = ""

if n1 == n2 == n3:
   risultato = "all the same"
elif n1 != n2 and n1 !=n3 and n2 != n3:
   risultato = "all different"
else: 
   risultato = "neither"

print(risultato)