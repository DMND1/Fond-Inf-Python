# Creare una matrice 10x10 con gli elementi della tabellina pitagorica

def vuota(n, m):
    matrice = []

    for i in range(n):
        riga = [0] * m
        matrice.append(riga)

    return matrice


def tabellinaPitagorica():
    pitagora = vuota(10,10)

    for i in range(10):
        for j in range(10):
            pitagora[i][j] = (i + 1) * (j + 1)

    return pitagora

tp = tabellinaPitagorica()

for riga in tp:
    for elem in riga:
        print(elem, end=" ")
    print()



print()

def tabellinaPitagorica(n, m):
    pitagora = vuota(n, m)

    for i in range(len(pitagora)):
        for j in range(len(pitagora[0])):
            pitagora[i][j] = (i + 1) * (j + 1)

    return pitagora

tp = tabellinaPitagorica(2,2)

for riga in tp:
    for elem in riga:
        print(elem, end=" ")
    print()