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


# Come conto quante volte un carattere si trova in una stringa?
s1 = "deposito"
cont_s1 = 0

for i in s1:
    cont_s1 = 0
    for c in s1:
        if i == c:
            cont_s1 += 1
    print(cont_s1)

print(cont_s1)


# Come conto quante volte un carattere si trova in due stringhe?
s1 = "odepoositoxx"
s2 = "xxdeopsitooo"
cont_s1 = 0
cont_s2 = 0
anagramma = True

for i in s1:
    cont_s1 = 0
    cont_s2 = 0
    for c in s1:
        if c == i:
            cont_s1 += 1
    print(cont_s1)
    for x in s2:
        if x == i:
            cont_s2 += 1
    print(cont_s2)
    if cont_s1 != cont_s2:
        anagramma = False

print(anagramma)


# Il programma senza usare .count() diventerebbe:
s1 = input("Inserire la stringa 1: ")
s2 = input("Inserire la stringa 2: ")

# Controllo se le stringhe hanno la stessa lunghezza
if len(s1) != len(s2):
    print("Le due stringhe non sono anagrammi")
# Altrimenti
else:
    # Inizializzazione varabili, presumiamo che le due stringhe siano anagrammi
    anagramma = True
    # cont_s1 = 0   # questi contatori possono non essere azzerati ogni volta all'interno del ciclo for che segue, quindi se non si mettono lì, bisogna metterli qui
    # cont_s2 = 0   # in questo programma però non serve
    for i in s1:
        cont_s1 = 0
        cont_s2 = 0
        for c in s1:
            if c == i:
                cont_s1 += 1
        for x in s2:
            if x == i:
                cont_s2 += 1
        if cont_s1 != cont_s2:
            anagramma = False
    # Se anagramma è rimasto True, vuol dire che ogni lettera di s1 non solo si trova in s2 ma si strova in s2 lo stesso numero di volte che si trova in s1
    if anagramma == True:
        print("Le due stringhe sono anagrammi")
    # Altrimenti
    else:
        print("Le due stringhe non sono anagrammi")

# Oss: se una lettera si trova n volte nella prima stringa e n volte nella seconda, allora se sì tolgono da entrambe le stringhe queste due avranno la stessa lunghezza

# Quindi il programma si può scrivere anche in questo modo:

s1 = input("Inserire la stringa 1: ")
s2 = input("Inserire la stringa 2: ")

# Controllo se le stringhe hanno la stessa lunghezza
if len(s1) != len(s2):
    print("Le due stringhe non sono anagrammi")
# Altrimenti
else:
    # Inizializzazione varabili, presumiamo che le due stringhe siano anagrammi
    anagramma = True
    for i in s1:
        s1 = s1.replace(i,"")
        s2 = s2.replace(i,"")
        if len(s1) != len(s2):
            anagramma = False
     if anagramma == True:
        print("Le due stringhe sono anagrammi")
        # Altrimenti
     else:
        print("Le due stringhe non sono anagrammi")



# Contare quante volte la lettera p è contenuta in s

c = "p"
s = "paperino"

conta = 0

for e in s:
    if e == c:
        conta += 1