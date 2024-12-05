# Creare una matrice quadrata N 10×10 per cui alla riga i-esima e alla colonna j-esima sia memorizzato il valore i - j

def vuota(n, m):
    matrice = []

    for i in range(n):
        riga = [0] * m
        matrice.append(riga)

    return matrice

def matrice10x10():
    N = vuota(10, 10)

    for i in range(10):
        for j in range(10):
            N[i][j] = i - j

    return N

N = matrice10x10()

for riga in N:
    for elem in riga:
        if "-" in str(elem):
            print(elem, end="  ")
        else:
            print(elem," ", end=" ")
    print()