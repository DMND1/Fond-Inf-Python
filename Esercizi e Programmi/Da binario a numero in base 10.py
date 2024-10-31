# L'utente batte una stringa di 4 cifre binarie (per esempio "1011"), scrivere il numero corrispondente in base 10 usando gli if

n = input("Numero in binario di 4 cifre: ")

# Ricordandosi come si passa dalla base 2 alla base 10 e usando gli if:

risultato = 0

# si noti come il seguente if statement può essere omesso:
# if n[0] == 0:
#     risultato = risultato + 0     # Che equivale a pass

if n[0] == "1":
    risultato = risultato + 2**3
if n[1] == "1":
    risultato = risultato + 2**2
if n[2] == "1":
    risultato = risultato + 2**1
if n[3] == "1":
    risultato = risultato + 2**0

print("Il numero in base 10 è:", risultato)


# In alternativa se si vogliono fare tutti i casi:

# Pseudo codice: 
# leggi numero
# se i primi 3 numeri sono zero:
#   se l'ultimo numero è 0:
#       stampa 0
#   altrimenti:
#       stampa 1
# altrimenti se i primi 2 numeri sono zero:
#   se l'ultimo numero è 0:
#       stampa 2
#   altrimenti:
#       stampa 3
# altrimenti se il primo numero è zero:
#   se l'ultimo numero è 0:
#       stampa 2
#   altrimenti:
#       stampa 3
# ...

if n[0] == n[1] == n[2] == "0":     # in alternativa si può scrivere n[0] == "0" and n[1] == "0" and n[2] == "0"
    if n[3] == "0" :
        risultato = 0
    else:
        risultato = 1

elif n[0] == n[1] == "0":
    if n[3] == "0" :
        risultato = 2
    else:
        risultato = 3

elif n[0] == "0":
    if n[2] == n[3] == "0" :
        risultato = 4
    elif n[2] == "0" and n[3] == "1":
        risultato = 5
    elif n[2] == "1" and n[3] == "0":
        risultato = 6
    else:
        risultato = 7

else:
    if n[1] == n[2] == n[3] == "0":
        risultato = 8
    elif n[1] == n[2] == "0" and n[3] == "1":
        risultato = 9
    elif n[1] == n[3] == "0" and n[2] == "1":
        risultato = 10
    elif n[1] == "0" and n[3] == n[2] == "1":
        risultato = 11
    elif n[1] == "1" and n[3] == n[2] == "0":
        risultato = 12
    elif n[1] == n[3] == "1" and n[2] == "0":
        risultato = 13
    elif n[1] == n[2] == "1" and n[3] == "0":
        risultato = 14
    else:
        risultato = 15


print("Il numero in base 10 è:", risultato)