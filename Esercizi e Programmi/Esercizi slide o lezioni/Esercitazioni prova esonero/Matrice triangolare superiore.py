# Scrivere una funzione in PYthon che abbia come parametro una matrice quadrata m e che restituisca True o False a seconda che la matrice sia 
# traingolare superiore o meno

def triangSup(matrice):
    for i in range(1, len(matrice)):
        for j in range(0, i):
            if matrice[i][j] != 0:
                return False
    return True