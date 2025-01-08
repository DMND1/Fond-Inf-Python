def matriceIdentita(matrice):

    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if i == j and matrice[i][j] != 1:
                return False
            elif i != j and matrice[i][j] != 0:
                return False

    return True

mat1 = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

mat2 = [
    [1,0,2],
    [0,0,0],
    [0,0,1]
]

print(matriceIdentita(mat1))
print(matriceIdentita(mat2))