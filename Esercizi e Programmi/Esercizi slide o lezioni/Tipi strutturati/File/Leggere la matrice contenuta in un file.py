# Programma per scrivere su un file
f_mat = open("Esercizi e Programmi\Esercizi slide o lezioni\Tipi strutturati\File\matrice.txt", "w")

f_mat.write("2 7 5 \n")
f_mat.write("3 4 1")

f_mat.close()



# Programma per leggere un file
f_mat = open("Esercizi e Programmi\Esercizi slide o lezioni\Tipi strutturati\File\matrice.txt")     # senza secondo parametro è in lettura di default

riga = f_mat.readline()

lista = riga.split()

for i in range(len(lista)):
    lista[i] = int(lista[i])

f_mat.close()

print(lista)
print()



# Su un file c'è scrittta una matrice, vogliamo leggerla e restituire la matrice
def leggiMatrice(nome_file):
    matrice = []
    f_mat = open(nome_file, "r")

    for linea in f_mat:

        lista = linea.split()

        for i in range(len(lista)):
            lista[i] = int(lista[i])
        
        matrice.append(lista)
    
    f_mat.close()

    return matrice

print(leggiMatrice("Esercizi e Programmi\Esercizi slide o lezioni\Tipi strutturati\File\matrice.txt"))



# Fare una funzione che data una matrice e il nome di un file scriva la matrice dentro il file