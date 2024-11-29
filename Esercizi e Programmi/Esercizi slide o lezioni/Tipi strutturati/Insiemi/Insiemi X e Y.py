# Scrivere un progamma che costruisca gli insiemi X dei quadrati minori di 1000 e l’insieme Y dei cubi minori di 1000 e verifichi se esiste un naturale il cui predecessore è un 
# quadrato e il cui successore è un cubo.
limite = 1000
X = set()
Y = set()

i = 1
while (i ** 2) < limite:
    X.add(i ** 2)
    i += 1

i = 1
while (i ** 3) < limite:
    Y.add(i ** 3)
    i += 1

intersezione = set()

for elememnto_y in Y:
    for elemento_x in X:
        if (elememnto_y - 1) == (elemento_x + 1):
            intersezione.add(elememnto_y - 1)

print(intersezione)



# O in alternativa:
for cubo in Y:
    if (cubo - 2) in X:
        intersezione.add(cubo - 1)

print(intersezione)



# O in alternativa:
predecessori_quadrati = set()
successori_cubi = set()

for elem in X:
    predecessori_quadrati.add(elem + 1)

for elem in Y:
    successori_cubi.add(elem - 1)

intersezione = predecessori_quadrati.intersection(successori_cubi)
print(intersezione)



# O in alternativa: 
predecessori_quadrati = set()
successori_cubi = set()

i = 1
while (i ** 2) < limite:
    predecessori_quadrati.add(i ** 2 + 1)
    i += 1

i = 1
while (i ** 3) < limite:
    successori_cubi.add(i ** 3 - 1)
    i += 1

intersezione = predecessori_quadrati.intersection(successori_cubi)
print(intersezione)