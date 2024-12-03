# Data una lista, eliminare le copie degli elementi che appaiono due volte o più
lista = [2, 2, 3, 1, 5, 4, 5, 5, 2, 2, 2]

def removeCopies(lista):
    insieme = set(lista)

    for numero in insieme:
        contatore = lista.count(numero)
        i = len(lista) - 1
        while i >= 0 and contatore > 1:
            if lista[i] == numero:
                lista.pop(i)
                contatore -= 1
            i -= 1

    return lista

print(removeCopies(lista))



# Data una lista, eliminare gli elementi che appaiono due volte o più
lista = [2, 2, 3, 1, 5, 4, 5, 2, 2, 2, 2]

def removeCopies(lista):
    insieme = set(lista)

    for numero in insieme:
        contatore = lista.count(numero)
        if contatore > 1:
            for i in range(contatore):
                lista.remove(numero)

    return lista

print(removeCopies(lista))