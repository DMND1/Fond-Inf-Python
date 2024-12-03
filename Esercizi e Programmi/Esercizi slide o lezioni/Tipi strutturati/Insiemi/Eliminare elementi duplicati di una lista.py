# Data una lista, eliminare gli elementi che appaiono due volte o più

lista = [4, 2, 3, 1, 5, 5, 2, 2, 2, 2]

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

# Data una lista, eliminare le copie degli elementi che appaiono due volte o più
lista = [4, 2, 3, 1, 5, 5, 2, 2, 2, 2]

def removeCopies(lista):
    insieme = set(lista)

    for numero in insieme:
        contatore = lista.count(numero)
        if contatore >= 2:
            for i in range(contatore):
                lista.remove(numero)

    return lista

print(removeCopies(lista))