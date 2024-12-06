# Data una lista, l'utente immete un valore e bisogna togliere tutte le comparse di quel valore dalla lista

lista = [1, 2, 3, 4, 5, 5, 2, 2, 2, 2]

def removeDuplicates(lista, s):
    l = []

    for i in lista:
        if i != s:
            l.append(i)
    
    return l

print(removeDuplicates(lista, 2))
print(removeDuplicates(lista, 5))

def rimuoviDuplicati(l, s):
    i = 0
    while i < len(l):
        if l[i] == s:
            l.pop(i)
        else:
            i += 1
    
    return l

print(rimuoviDuplicati(lista, 2))

lista = [1, 2, 3, 4, 5, 5, 2, 2, 2, 2]
print(rimuoviDuplicati(lista, 5))