# Data una lista, eliminare gli elementi che appaiono due volte o più

lista = [1,2,3,4,5,5,2,2,2,2]

def removeDuplicates(lista):
    copia = list(lista)

    duplicati = set()

    for i in lista:
        copia.remove(i)
        if i in copia:
            duplicati.add(i)

    lista = set(lista)
    lista = lista.difference(duplicati)
    lista = list(lista)

    return lista

print(removeDuplicates(lista))