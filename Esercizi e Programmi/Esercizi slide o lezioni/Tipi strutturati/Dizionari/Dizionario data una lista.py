# Data una lista di parole

# chiave: parola
# ad ogni parola(chiave) associo quanto volte si trova nel dizionario

lista = ["casa", "dolce", "casa"]

dizionario = {}

for elem in lista:
    dizionario[elem] = lista.count(elem)

print(dizionario)


# Per ogni p di parole
#   se P è nel dizionario:
#       d[p] += 1
#   altrimenti:
#       d[p] = 1

parole = ["casa", "dolce", "casa"]
d = {}

for p in parole:
    if p in d:
        d[p] += 1
    else:
        d[p] = 1

print(d)

# Per rendere il codice più comprensibile:
d = {}

for p in parole:
    if p not in d:
        d[p] = 1
    else:
        d[p] += 1

print(d)

# Programma senza if:
d = {}

for p in parole:
    d[p] = d.get(p, 0) + 1

print(d)