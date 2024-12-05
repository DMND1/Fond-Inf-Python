# Date due matrici controllare se sono l'una la trasposta dell'altra

matA = [
    [1, 2, 1],
    [1, 2, 1],
    [1, 1, 1]
]
matB = [
    [1, 1, 1],
    [2, 2, 1],
    [1, 1, 1]
]

def trasposta(matA, matB):
    if len(matA) != len(matB) or len(matA[0]) != len(matB[0]):
        return False
    
    for i in range(len(matA)):
        for j in range(len(matA)):
            if matA[i][j] != matB[j][i]:
                return False
    
    return True

print(trasposta(matA, matB))