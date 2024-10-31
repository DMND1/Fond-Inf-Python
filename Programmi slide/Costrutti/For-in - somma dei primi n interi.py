# Somma da 1 a n, questa somma è n (n+1) / 2, calcolare la somma senza la formula di Gauss

# s = somma parziale
# il prossimo valore di s sarà = s + i da cui s = s + i

n = int(input("Numeri da sommare: "))

s = 0   # In ogni momento s contiene le somme parziali

for i in range(1, n+1):
    s = s + i

print("La somma di tutti i nueri da 0 a", n, "è", s)    # Stampa la somma dei primi n interi