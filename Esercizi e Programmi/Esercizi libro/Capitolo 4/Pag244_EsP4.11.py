# Scrivete un programma che legga una prola e visualizzi il numero di sillabe presenti in essa. Per questo esercizio assumente che, in inglese, le sillabe siano così definite:
# qualsiasi sequenza di vocali adiacenti (e le vocali sono a e i o u y) è una sillaba, tranne una "e" a fine parola. Se, però, questo algoritmo porta a un conteggio pari a zero, 
# fornite come risultato il valore 1

# Esempi:
# Harry : "a" e "y" sono vocali singole : sillabe = 2
# Hairy : "ai" e "y" sono risp. vocali adiacienti e vocale singola : sillabe = 2
# hare : "a" e "e" vocale singola ed "e" alla fine : silalbe = 1
# the : "e" alla fine : sillabe = 1

# Oss: Problema: ad esempio la parola "Queueing" ha due sillabe ma seguendo la definizione del libro ne dovrebbe avere solo una


# Obiettivo: contare quante volte ci sono vocali singole o adiacienti in una parola

# Pseudocodice:
# num_sillabe = 0
# consonanti = "bcdfghjklmnpqrstvwxyz"
# rimuovi tutte le consonanti da una parola e rimpiazzale con "."
# conta quante volte (x) ci sono delle vocali comprese tra due punti (.a.) o comprese tra un punto e la fine della parola (.a), se quest'ultima vocale è una "e" non contarla
# num_sillabe += x
# stampa num_sillabe

parola = input("Inserire una parola: ")
parola = parola.lower()

# Inizializzazione variabili per rimuovere le consonanti
consonanti = "bcdfghjklmnpqrstvwxz"

# Rimuovo le consonanati della parola e le rimpiazzo con "."
for c in consonanti:
    parola = parola.replace(c,".")

# Inizializzazione variabili per conteggio sillabe
num_sillabe = 0

# Conteggio delle sillabe fino a len(parola)-2
for i in range(len(parola)-2):    # i va da 0 a 4 (escluso)
    # Se il carattere di posizione i è una consonante: ossia se è "."
    if parola[i] == ".":
        # Se il carattere di posizone i+1 è una vocale
        if parola[i+1] != ".":
            # Addiziono 1 al numero delle sillabe
            num_sillabe += 1

# Poché se l'ultima lettera è una "e" non bisogna contarla, faccio l'ultimo caso separatamente fuori dal ciclo
if parola[len(parola)-2] == ".":
    # Se il carattere di posizone (len(parola)-1) è una vocale ma non è una e
    if parola[len(parola)-1] != "." and parola[len(parola)-1] != "e":
        # Addiziono 1 al numero delle sillabe
        num_sillabe += 1

# Se il numero di sillabe calcolato è 0, il risultato deve essere 1
if num_sillabe == 0:
    num_sillabe = 1
    print("Il numero di sillabe è:", num_sillabe)
# Altrimenti stampa il risultato calcolato
else:
    print("Il numero di sillabe è:", num_sillabe)