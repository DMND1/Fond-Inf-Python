# Scrivete la funzione sameSet(a,b) che verifichi se due liste contengono gli stessi elementi, indipendentemente dall'ordine e ingorando la presenza di duplicati

def sameSet(a,b):
    lista_a = []
    lista_b = []

    for i in a:
        if i not in lista_a:
            lista_a.append(i)

    for c in b:
        if c not in lista_b:
            lista_b.append(c)

    if lista_a == lista_b:
        return True
    else: 
        return False


lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 5]
lista2 = [1, 2, 3, 4, 5, 4, 3, 2, 5, 1, 1, 1, 1, 1]

print(sameSet(lista1, lista2))  # Stampa True


lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 5]
lista2 = [1, 2, 3, 4, 5, 4, 3, 2, 5, 1, 1, 1, 1, 1, 6]

print(sameSet(lista1, lista2))  # Stampa False