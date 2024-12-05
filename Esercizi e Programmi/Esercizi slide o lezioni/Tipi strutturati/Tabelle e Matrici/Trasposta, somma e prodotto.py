def vuota(n, m):
    matrice = []

    for i in range(n):
        riga = [0] * m
        matrice.append(riga)

    return matrice

def tabellinaPitagorica(n, m):
    pitagora = vuota(n, m)

    for i in range(len(pitagora)):
        for j in range(len(pitagora[0])):
            pitagora[i][j] = (i + 1) * (j + 1)

    return pitagora

def matrice10x10():
    N = vuota(10, 10)

    for i in range(10):
        for j in range(10):
            N[i][j] = i - j

    return N

M = tabellinaPitagorica(10, 10)
N = matrice10x10()



# Trasposta di una matrice
def trasposta(matrice):

    trasposta = vuota(len(matrice), len(matrice[0]))

    for i in range(len(trasposta)):
        for j in range(len(trasposta[0])):
            trasposta[i][j] = matrice[j][i]
    
    return trasposta

for riga in N:
    for elem in riga:
        if "-" in str(elem):
            print(elem, end="  ")
        else:
            print(elem," ", end=" ")
    print()

print()

trasposta_N = trasposta(N)

for riga in trasposta_N:
    for elem in riga:
        if "-" in str(elem):
            print(elem, end="  ")
        else:
            print(elem," ", end=" ")
    print()

print()


# Somma di matrici
def sommaMatrici(matA, matB):
    if len(matA) != len(matB) or len(matA[0]) != len(matB[0]):
        return None

    somma = vuota(len(matA), len(matA))

    for i in range(len(matA)):
        for j in range(len(matA)):
            somma[i][j] = matA[i][j] + matB[i][j]
    
    return somma

somma_N_M = sommaMatrici(N, M)

for riga in somma_N_M:
    for elem in riga:
        if "-" in str(elem):
            print(elem, end="  ")
        else:
            print(elem," ", end=" ")
    print()

print()



# Prodotto di matrici
def prodotto(matA, matB):

    mat_prodotto = vuota(len(matA), len(matB[0]))
    
    for i in range(len(matA)):
        for j in range(len(matB[0])):
            for k in range(len(matA[0])):  
                mat_prodotto[i][j] += matA[i][k] * matB[k][j]

    return mat_prodotto

A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]

prodotto_A_B = prodotto(A, B)

for riga in prodotto_A_B:
    for elem in riga:
        print(elem, end=" ")
    print()

print()

prodotto_N_M = prodotto(N, M)

for riga in prodotto_N_M:
    for elem in riga:
        print(elem, end=" ")
    print()