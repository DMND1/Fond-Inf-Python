# Scrivete la funzione sameElements(a,b) che verifichi se due liste contengono lo gli stessi elementi con le stesse molteplicità, indpendentemente dall'ordine

# con sort:
def sameElements(a,b):
    a.sort()
    b.sort()
    if a == b:
        return True
    else: 
        return False


# con count:
def sameElements(a,b):
    if len(a) != len(b):
        return False

    for i in a:
        cont_a = 0
        cont_b = 0

        cont_a = a.count(i)
        cont_b = b.count(i)

        if cont_a != cont_b:
            return False
    
    return True    


# senza sort e count: 
def sameElements(a,b):
    if len(a) != len(b):
        return False

    for i in a:
        cont_a = 0
        cont_b = 0

        for c in range(len(a)):
            if i == a[c]:
                cont_a += 1
            if i == b[c]:
                cont_b += 1

        if cont_a != cont_b:
            return False
    
    return True

lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 5]
lista2 = [3, 1, 2, 5, 4, 4, 3, 5, 2]

print(sameElements(lista1, lista2)) # Stampa True

lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 5]
lista2 = [3, 1, 2, 5, 4, 4, 3, 2, 2]

print(sameElements(lista1, lista2)) # Stampa False