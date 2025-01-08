
def primaF(nome_file):
	file = open(nome_file, "r")
	matrice = []

	for riga in file:
		lista_str = riga.split()
		
		for i in range(len(lista_str)):
			lista_str[i] = int(lista_str[i])
		
		lista_int = lista_str

		matrice.append(lista_int)
	
	return matrice

def secondaF(matrice):
	lista_diagonale = []

	for i in range(len(matrice)):
		for j in range(len(matrice)):
			if i == j:
				lista_diagonale.append(matrice[i][j])

	return lista_diagonale

print(primaF(r"C:\Fond-Inf-Python\Risorse\Prove4txt"))
matrice = primaF(r"C:\Fond-Inf-Python\Risorse\Prove4txt")
print(secondaF(matrice))
lista_diagonale = secondaF(matrice)

somma = 0
for numero in lista_diagonale:
	somma += numero

print("la media è: " + str(round(somma / len(lista_diagonale),2)))