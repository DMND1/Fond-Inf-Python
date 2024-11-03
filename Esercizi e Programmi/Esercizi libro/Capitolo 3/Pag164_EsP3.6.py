# Risolvete nuovamente l'esercizio precedente ma, prima di leggere i numeri, chiedete all'utente se l'ordine crescente/decrescente va verificato in senso "stretto" oppure no.
# Nel secondo caso, ovviamnete, la sequenza 3 4 4 è considerata crescente, così come la sequenza 4 4 4, che è anche decrescente
# 
# Pseudocodice:
# chiedere se in senso stretto o in senso lato
# leggi n1
# leggi n2
# leggi n3
# risultato = ""
# se in senso stretto: 
#   se n1 < n2 < n3:
#       risultato = "increasing"
#   altrimenti se n1 > n2 > n3:
#       risultato = "decreasing"
#   altrimenti:
#       risultato = "neither"
# se in senso lato:
#   se n1 <= n2 <= n3 and n1 != n3:
#       risultato = "increasing"
#   altrimenti se n1 >= n2 >= n3 and n1 != n3:
#       risultato = "decreasing"
#   altrimenti se n1 == n2 == n3:
#       risultato = "both increasing and decrasing"
#   altrimenti:
#       risultato = "neither"

domanda = input("scrivere: stretto o lato; se si intende trovare l'ordine dei tre numeri rispetivamente in senso stretto o lato: ")

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

risultato = ""

if domanda == "stretto":
    if n1 < n2 < n3:
        risultato = "increasing"
    elif n1 > n2 > n3:
        risultato = "decreasing"
    else:
        risultato = "neither"

elif domanda == "lato":
  if n1 <= n2 <= n3 and n1 != n3:
      risultato = "increasing"
  elif n1 >= n2 >= n3 and n1 != n3:
      risultato = "decreasing"
  elif n1 == n2 == n3:
      risultato = "both increasing and decrasing"
  else:
      risultato = "neither"

print(risultato)