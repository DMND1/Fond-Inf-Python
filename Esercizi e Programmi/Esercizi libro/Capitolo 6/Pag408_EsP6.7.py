# Scrivete la funzione removeMin che elimini da una lista il valore minimo senza usare né la funzione min né il metodo remove

def removeMin(lista):
    minimo = lista[0]
    indice_minimo = 0
    
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            indice_minimo = i
    
    lista.pop(indice_minimo)

    return lista

lista = [1, 2, 3, 4, 5, 4, 3, 2, 5]

print(lista)
print(removeMin(lista))