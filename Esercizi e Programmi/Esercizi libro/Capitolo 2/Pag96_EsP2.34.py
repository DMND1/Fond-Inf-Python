# Lo pseudocodice seguente descrive come estrarre, da un prezzo espresso mediante un numero in virgola mobile, il numero di dollari e il numero di centesimi.
# Ad esempio, dato un prezzo di 2.95 dollari, si ottentono i valori 2 e 95, rispettivamente per i dollarri e i centesimi

# Convertire il prezzo in numero intero e memorizzarlo nella varabile dollari
# Moltiplicare per 100 la differenza prezzo - dolari e aggiungervi 0.5
# Convertire il risutlato in numero intero e memorizzarlo nella variabile centesimi

# Traducete queto pseudocodice in programma Python che acquisisca un prezzo in ingresso e ne visualizzi i dollari e i centesimi. 
# Collaudate il programma con i prezzi 2.95 e 4.35

prezzo = float(input("Il prezzo da convertire è: "))

dollari = int(prezzo)
centesimi = int(100 * (prezzo - dollari) + 0.5)

print("Il prezzo convertito sarà:", dollari, "dollari e", centesimi, "centesimi")