# Scrivete la funzione sumWithoutSmallest che calcoli, con un solo ciclo, la somma di tutti i valori di una lista, escludendo il valore minimo. 
# Nel ciclo, aggiorante la somma e il valore minimo, al termine, restituite la differeneza tra questi due valori

def sumWithoutSmallest(lista):
    somma = 0
    minimo = lista[0]

    for i in lista:
        somma += i
        if i < minimo:
            minimo = i

    somma_senza_minimo = somma - minimo
    
    return somma_senza_minimo

lista = [1, 2, 3, 4, 5, 4, 3, 2, 5]

print(sum(lista))
print(sumWithoutSmallest(lista))