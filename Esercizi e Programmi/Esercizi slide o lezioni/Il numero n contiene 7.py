# Controllare se un numero intero dato in ingresso contenga la cifra 7

# Pesudocodice:
# leggi n
# risultato = "falso"
# se la prima cifra di n è 7:
#   risultato = "vero"
# altrimenti se la seconda cifra di n è 7:
#   risultato = "vero"
# ...
# altrimenti se l'ultima cifra di n è 7:
#   risultato = "vero"
# altrimenti (se nessuna cifra di n è 7, per esclusione):
#   pass, poiché abbaimo già assegnato a risultato la stringa "falso"

# Implementare, all'interno di un ciclo for, una catena di if:

n = str(input("Il numero intero é: "))  # Stiamo dando per scontato che l'utente immetta effettivamente un numero intero

risultato = "falso"

# n = "1234567"
# len(n) = 7
# n[6] = "7"

for i in range(0,len(n)):
    if n[i] == "7":
        risultato = "vero"

print("È", risultato, "che il numero contine la cifra 7")