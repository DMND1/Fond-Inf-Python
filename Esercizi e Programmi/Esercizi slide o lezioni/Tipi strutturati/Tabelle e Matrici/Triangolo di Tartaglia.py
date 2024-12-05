# Scrivere un programma che dato un vettore di n elementi (n chiesto all’utente) costituito da un 1 seguito da tutti 0, costruisca una tabella T n×n che abbia 
# come prima riga il vettore, prima colonna tutti 1 e come valore T[i][j] il valore T[i-1][j-1]+ T[i-1][j], per i≥1 e j≥1

n = int(input("Numero: "))

def primaColonna1(n, m):
    matrice = []

    for i in range(n):
        riga = [1] + [0] * (m-1)
        matrice.append(riga)

    return matrice


def triangoloDiTartaglia(n):
    T = primaColonna1(n,n)

    for i in range(1, n):
        for j in range(1, n):
            T[i][j] = T[i-1][j-1]+ T[i-1][j]

    return T

triangoloTartaglia = triangoloDiTartaglia(n)

for riga in triangoloTartaglia:
    for elem in riga:
        print(elem, end=" ")
    print()