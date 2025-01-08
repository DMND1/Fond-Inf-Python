# Illustrare la complessità computazionale di un programma che ordina gli elementi di una lista di interi positivi e poi cerca la mediana (risultato in O(n))

# se si usa il merge sort la prima parte del programma avrà come complessità computazionale O(nlogn)

# per cercare la mediana si fa in questo modo

lista = []

if len(lista) % 2 == 0:
    mediana = lista[len(lista)//2 - 1] + lista[len(lista)//2]
else:
    mediana = lista[len(lista)//2]

# la complessità computazionale di tale sottoprogramma è O(1)

# La complessità computazionale complessiva del programma sarà la somma delle due, ma poiché nlogn > 1 si ha come complessità complessiva O(nlogn)