# Fattorizzazione di interi. Scrivete un programma che chieda all'utente un numero intero e ne visualizzi i fattori. Se ad esempio l'utente fornisce il numero 150, 
# il programma deve visualizzare:
# 2
# 3
# 5
# 5

# Pseudocodice:
# leggi n
# ripetere per tutti i divisori tra 2 e n:
#   se il resto n % 2 è 0:
#       print(2)
#       n = n // 2
#   altrimenti se il resto n % 3 è 0:
#       print(3)
#       n = n // 2
#   ... ripetere fino a 
#   altrimenti se il resto n % n è 0:
#       print(n)    opppure     print("Il numero è primo")


n = int(input("Inserire un numero: "))

# Inizializzazione variabili
i = 2

# Inizio ciclo
while i <= n:
    # Se i è un divisore (intero) di n
    if n % i == 0:
        # Stampa i
        print(i)
        # Pongo n = al risultato di tale divisione intera
        n = n // i
        # Pongo i = 2, questo perché dobbiamo riniziare "da capo" a controllare tutti i divisori (interi) di n
        i = 2
    # Altrimenti se i non è un divisore di n
    else:
        # Incremento di 1 la variabile i, per provare il prossimo divisore intero
        i += 1


# In alternativa il programma si può anche scrivere così:
n = int(input("Inserire un numero: "))

# Inizializzazione variabili
i = 2

while i <= n:
    # Se i è un divisore (intero) di n
    if n % i == 0:
        # Stampa i
        print(i)
        # Pongo n = al risultato di tale divisione intera
        n = n // i
        # Pongo i = 2, questo perché dobbiamo riniziare "da capo" a controllare tutti i divisori (interi) di n
        i = 1
    # Altrimenti se i non è un divisore di n incremento di 1 la variabile i, per provare il prossimo divisore intero
    i += 1