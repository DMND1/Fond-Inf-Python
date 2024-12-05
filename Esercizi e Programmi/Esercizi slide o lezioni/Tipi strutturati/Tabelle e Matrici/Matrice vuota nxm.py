# Scriver una funzione che crei una matrice di n righe e m colonne

def vuota(n, m):
    matrice = []

    for i in range(n):
        riga = [0] * m
        matrice.append(riga)

    return matrice

print(vuota(10, 10))