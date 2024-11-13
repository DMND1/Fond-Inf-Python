# vedere se due stringhe sono uno l'anagramma dell'altro anche se le lettere sono ripetute

# Pseudocodice:
# leggi stringa1
# leggi stringa2
# Per ogni lettera di stringa1 conta quante volte compare in stringa1
# Per la stessa lettera conta quante volte compare in stringa2
# Se i due contatori sono uguali per tutte le lettere allora le due stringe sono anagrammi 
# (se un contatore è 0 e un altro è 1 per esempio, anche in questo caso non sono uguali e vuol dire che una lettera non è contenuna in una parola 
# ma nell'altra si)ss

# in python c'è una funzione che conta le ricorrenze di una certo carattere in una stringa: stringa1.count(".")

s1 = input("Inserire la stringa 1: ")
s2 = input("Inserire la stringa 2: ")

# controllare se le stringhe hanno la stessa lunghezza
if len(s1) != len(s2):
    print("Le due stringhe non sono anagrammi")
# Altrimenti
else:
    # Inizializzazione varabili, presumiamo che le due stringhe siano anagrammi
    anagramma = True
    # Per ogni lettera in s1
    for c in s1:
        # Se tale lettera non compare in s1 e in s2 lo stesso numero di volte
        if s1.count(c) != s2.count(c):
            # Allora le due stringhe non sono anagrammi
            anagramma = False
            # In teoria break serve solo per rendere il programma più efficiente ma non è necessario
            break
    # Se anagramma è rimasto True, vuol dire che ogni lettera di s1 non solo si trova in s2 ma si strova in s2 lo stesso numero di volte che si trova in s1
    if anagramma == True:
        print("Le due stringhe sono anagrammi")
    # Altrimenti
    else:
        print("Le due stringhe non sono anagrammi")


# Il programma senza usare .count() diventerebbe: ... Da finire

s1 = input("Inserire la stringa 1: ")
s2 = input("Inserire la stringa 2: ")

# controllare se le stringhe hanno la stessa lunghezza
if len(s1) != len(s2):
    print("Le due stringhe non sono anagrammi")
# Altrimenti
else:
    # Inizializzazione varabili, presumiamo che le due stringhe siano anagrammi
    anagramma = True


# Come conto quante volte un carattere si trova in una stringa? ... Da finire
s1 = "deposito"
s1 = "deposito"
cont_s1 = 0

for i in s1:
    s1 = s1.replace(i, ".")
    for c in s1:
        if c == ".":
            cont_s1 += 1
    s1 = s1.replace(".","")

print(cont_s1)