# input per matrici: ogni lista corrisponde ad una riga

# Per semplicità controlliamo due matrici 2x2
numero_righe = 2
numero_colonne = 2
riga1_matA = []
riga2_matA = []
riga1_matB = []
riga2_matB = []

# Input matrice A
print("Numeri della prima riga di A")
for i in range(1, numero_colonne + 1):
    n = int(input("Inserire un numero: "))
    riga1_matA.append(n)
i = 0

print("Numeri della seconda riga di A")
for i in range(1, numero_colonne + 1):
    n = int(input("Inserire un numero: "))
    riga2_matA.append(n)
i = 0

# Input matrice B
print("Numeri della prima riga di B")
for i in range(1, numero_colonne + 1):
    n = int(input("Inserire un numero: "))
    riga1_matB.append(n)
i = 0

print("Numeri della seconda riga di B")
for i in range(1, numero_colonne + 1):
    n = int(input("Inserire un numero: "))
    riga2_matB.append(n)
i = 0

print("Matrice A:")
print(riga1_matA)
print(riga2_matA, "\n")
print("Matrice B:")
print(riga1_matB)
print(riga2_matB)

def MatriceTrasposta(riga1_matA, riga2_matA, riga1_matB, riga2_matB):
    nuova_riga1_matA = riga1_matA[0] + riga2_matA[0]
    nuova_riga2_matA = riga1_matA[1] + riga2_matA[1]

    nuova_riga1_matB = riga1_matB[0] + riga2_matB[0]
    nuova_riga2_matB = riga1_matB[1] + riga2_matB[1]

    if nuova_riga1_matA == nuova_riga1_matB and nuova_riga2_matA == nuova_riga2_matB:
        return True
    else:
        return False

print(MatriceTrasposta(riga1_matA,riga2_matA,riga1_matB,riga2_matB))

# In alternativa
MatA = [riga1_matA, riga2_matA]
MatB = [riga1_matB, riga2_matB]

def MatriceTrasposta2(MatA, MatB):
    nuova_matA = [MatA[0][0] + MatA[1][0]] + [MatA[0][1] + MatA[1][1]]

    nuova_matB = [MatB[0][0] + MatB[1][0]] + [MatB[0][1] + MatB[1][1]]

    if nuova_matA == nuova_matB:
        return True
    else:
        return False

print(MatriceTrasposta2(MatA,MatB))