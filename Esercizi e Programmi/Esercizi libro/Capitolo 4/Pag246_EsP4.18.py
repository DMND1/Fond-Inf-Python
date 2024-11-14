# Scrivete un programma che visualizzi una tavola pitagorica, come questa:
#   1   2   3   4   5   6   7   8   9   10
#   2   4   6   8   10  12  14  16  18  20
# ...
#   10  20  30  40  50  60  70  80  90  100

# Oss: la differenza tra 2 e 1 = 1
# la differenza tra 4 e 2 = 2 ...
# Ossia il passo è uguale al primo numero della sequenza

# Inizializzazione variabili
risposta = ""

# Inizio ciclo, la i è il primo numero della riga
for i in range(1, 11):
    # Inizio secondo ciclo, dove la variabile c parte da 1 e arriva fino a 10*i + 1 con passo i
    for c in range(i, 10*i + 1, i):
        # Modifica della risposta
        risposta += str(c) + "  "
    # Stampa la risposta
    print(risposta)
    # Reset variabili
    risposta = ""

print() # Metto uno spazio per distinguere i due programmi


# Formattazione (superflua) del codice:

# Inizializzazione variabili
risposta = ""

# Inizio ciclo, la i è il primo numero della riga
for i in range(1,11):
    # Inizio secondo ciclo, dove la variabile c parte da 1 e arriva fino a 10*i + 1 con passo i
    for c in range(i, 10*i + 1, i):
        # Se la lunghezza della stringa c è 1:
        if len(str(c)) == 1:
            # Modifica della risposta e aggiunta di 3 spazi
            risposta += str(c) + "   "
        # Altrimenti se la lunghezza della stringa c è 1:
        elif len(str(c)) == 2:
            # Modifica della risposta e aggiunta di 2 spazi
            risposta += str(c) + "  "
        # Altrimenti se la lunghezza della stringa c è 1:
        elif len(str(c)) == 3:
            # Modifica della risposta e aggiunta di 1 spazi
            risposta += str(c) + " "
    # Stampa la risposta
    print(risposta)
    # Reset variabili
    risposta = ""