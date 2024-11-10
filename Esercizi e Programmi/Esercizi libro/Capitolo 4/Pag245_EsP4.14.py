# Media e deviazione standard. Scrivete un programma che legga un insieme di valori in virgola mobile. Adottate il meccanismo più adeguato per consentire all'utente di 
# segnalare la fine dei dati. Quando tutti i valori sono stati acquisiti, visualizzatene il numero, il valore medio e la deviazione standard. Il valore medio è 
# la somma di tutti gli input / il numero di input. La deviazione standard, invece, è: 
# vedere libro
# Questa formula, però, non è addatta alla nostra elaborazione, ... Usate la seguente formula:
# vedere libro
# Con quest'ultima formula le deviazione standard viene calcolata aggiornando e memorizzando, via via che i valori vengono acquisiti, il numero di valori, 
# la loro somma e la somma dei loro quadrati

from math import sqrt

x = input("Inserire un numero: ")

if x == "stop":
    print("Errore")
else: 
    # Inizializzazione variabili (volendo quest'ultime possono essere inizializzate anche al di fuori della condizione if/else)
    cont = 0
    somma = 0
    somma_quad = 0
    # Inizio ciclo
    while x != "stop":
        # Converto x in float e aumento il contatore
        x = float(x)
        cont += 1
        # Calcolo della somma e della somma dei quadrati
        somma += x
        somma_quad += x**2
        x = input("Inserire un numero (altrimenti stop per fermare il programma): ")

# Calcolo della media e della deviazione standard
media = somma / cont
dev_standard = sqrt((somma_quad - (somma**2 / cont))/(cont - 1))

# Stampo il risultato
print("La media è:", media)
print("La deviazione standard è:", dev_standard)

# Esempio di esecuzione:
# Inserire un numero: 62
# Inserire un numero (altrimenti stop per fermare il programma): 65
# Inserire un numero (altrimenti stop per fermare il programma): 90
# Inserire un numero (altrimenti stop per fermare il programma): stop
# La media è: 72.33333333333333
# La deviazione standard è: 15.373136743466931