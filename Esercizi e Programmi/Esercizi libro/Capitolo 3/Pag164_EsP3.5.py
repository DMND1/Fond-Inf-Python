# Scrivete un programma che legga tre numeri e visualizzi il messaggio "increasing" se sono in ordine crescente, "decreasing" se sono in ordine decrescente e "neither" se non sono
# nè in ordine crescete nè in ordine decrescente. In questo esercizio crescente significa strettamente crescente, cioè ciasciun valore deve essere maggiore del precendete 
# (analog. per decresc), la sequenza 3 4 4, quindi, non va considerata crescente

# Pseudocodice:
# leggi n1
# leggi n2
# leggi n3
# risultato = ""
# se n1 < n2 < n3:
#   risultato = "increasing"
# altrimenti se n1 > n2 > n3:
#   risultato = "decreasing"
# altrimenti:
#   risultato = "neither"
# stampa il risultato

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

if n1 < n2 < n3:
  risultato = "increasing"
elif n1 > n2 > n3:
  risultato = "decreasing"
else:
  risultato = "neither"

print(risultato)