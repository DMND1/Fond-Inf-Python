# Scrivete un programma che legga un insieme di valori in virgola mobile e, poi, visualizzi:
# - la media dei valori
# - il valore massimo
# - il valore minimo
# - la dinamica dei valori, cioè la diferenza tra il valore massimo e il valore minimo

x = input("Inserire un numero: ")

if x == "":
    print("Nessun numero inserito")
else:
    # Definizione variabili:
    massimo = float(x)
    minimo = float(x)
    contatore = 0
    somma = 0
    # Inizio ciclo:
    while x != "":
        x = float(x)
        # Media:
        contatore += 1
        somma += x
        media = somma / contatore
        # Massimo e minimo:
        if x > massimo:
            massimo = x
        elif x < minimo:
            minimo = x
        # Dinamica:
        dinamica = massimo - minimo
        # Nuovo input:
        x = input("Inserire un numero (lasciare vuoto per terminare): ")
    # Arrotondamenti opportuni:
    massimo = round(massimo,2)
    minimo = round(minimo,2)
    media = round(media,2)
    dinamica = round(dinamica,2)
    # Stampa il risultato:
    print("La media è:", media)
    print("Il massimo è:", massimo)
    print("Il minimo è:", minimo)
    print("La dinamica dei valori è:", dinamica)