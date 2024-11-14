# Traducete in un programma Python la seguente descrizione in pseudocodice (vedi libro), che trova il valore minimo in un insieme di dati acquisiti in ingresso

x = input("Inserire un numero: ")
first = True

if x == "":
    print("Nessun numero inserito")
else:
    while x != "":
        x = int(x)
    # Controllo minimo:
        if first == True:
            minimum = x
            first = False
        elif x < minimum:
            minimum = x
    # Nuovo input:
        x = input("Inserire un numero (lasciare vuoto per terminare): ")
    # Stampa il risultato:
    print(minimum)