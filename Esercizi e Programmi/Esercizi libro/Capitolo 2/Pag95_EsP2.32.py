# Lo pseudocodice seguente descrive come, in una libreria, viene calcolato l'importo di un ordine a partire dal costo totale dei libri ordinati e dal loro numero.

# Leggere il costo totale dei libri e il numero di libri
# Calcolare le tasse (il 7.5 per cento del costo totale dei libri)
# Calcolare i costi di spedizione ($ 2 per ogni libro)
# II prezzo totale dell'ordine é la somma del costo totale dei libri, delle tasse e dei costi di spedizione
# Visualizzare limporto dell'ordine

# Traducete questo pseudocodice in un programma Python.

costo_totale_libri = float(input("Costo totale dei libri: "))
n_libri = int(input("Numero di libri: "))
tasse = 7.5 * costo_totale_libri / 100
spedizione = n_libri * 2

prezzo_totale = costo_totale_libri + tasse + spedizione

print("Il prezzo totale dell'ordine sarà:", prezzo_totale)