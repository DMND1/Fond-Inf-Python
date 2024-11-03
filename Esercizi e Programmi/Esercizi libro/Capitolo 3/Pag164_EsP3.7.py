# Scrivete un programma che legga tre numeri interi e visualizzi il messaggio "in order" se sono ordinati in senso crescente o descrescente (in senso lato) e "not in order"
#  in caso contrario. Ad esempio:
# 1 2 5     in order
# 1 5 2     not in order
# 5 2 1     in order
# 1 2 2     in order

# Pseudocodice: 
# leggi n1
# leggi n2
# leggi n3
# risultato = ""
# ... vedi programma precedente
# stampa risultato

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

risultato = ""

if n1 <= n2 <= n3:
    risultato = "in order"
elif n1 >= n2 >= n3:
    risultato = "in order"
else:
    risultato = "not in order"

print(risultato)