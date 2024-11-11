# date due stringhe vedere se una è un anagramma dell'altra, tutti i caratteri delle stringhe sono diversi
# Esempio: rosa, raso, orsa sono anagrammi

# se le due stringhe hanno la stessa lunghezza
#   se la prima lettera della stringa 1 è contenuta nella seconda e
#   se la sedonda lettera della stringa 1 è contenuna nella seconda e
#   ...
#   se tutte le lettere della stringa 1 sono contenuto nella secondo: allora la parola è palindroma

stringa1 = input("Inserire la stringa 1: ")
stringa2 = input("Inserire la stringa 2: ")

# Inizializzazione varabili
Anagramma = 0

# Controllo se le stringhe hanno la stessa lunghezza
if len(stringa1)==len(stringa2):
    # Ciclo che controlla ogni lettera di stringa1
    for i in range(0,len(stringa1)):
        # Se la lettera in posizione i della stringa1 è contenunta nella stringa2
        if stringa1[i] in stringa2:
        # Aumenta di 1 la variabile Anagramma
            Anagramma += 1

# Se la variabile anagramma è uguale alla lunghezza della stringa1(o stringa2) allora vuol dire che il ciclo ha trovato per ogni lettera in stringa1 la stessa lettera in stringa2
if Anagramma == len(stringa1):
    risposta = "Le due stringhe sono anagrammi"
# Altrimenti il ciclo ha trovato almeno una lettera non in comune tra le due stringhe, per cui quest'ultime non sono anagrammi
else:
    risposta = "Le due stringhe non sono anagrammi"

# Stampo la risposta
print(risposta)


# In altenativa (non so se va bene usare quanto scritto nella riga 46):
stringa1 = input("Inserire la stringa 1: ")
stringa2 = input("Inserire la stringa 2: ")

# Inizializzazione varabili
Anagramma = False

# Controllo se le stringhe hanno la stessa lunghezza
if len(stringa1)==len(stringa2):
    # Se tutte le lettere di stringa1 sono in stringa2
    if all (c in stringa1 for c in stringa2):
    # Allora le due parole sono anagrammi, il ciclo finisce
        Anagramma = True

# Se il ciclo non ha cambiato la variabile Anagramma in True, allora le due stringhe non sono anagrammi
if Anagramma == False:
    risposta = "Le due stringhe non sono anagrammi"
# Altrimenti le due stringhe sono anagrammi
else:
    risposta = "Le due stringhe sono anagrammi"

# Stampo la risposta
print(risposta)