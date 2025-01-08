def creazioneTriple(nome_file):
	file = open(nome_file, "r")
	lista = []
	
	for riga in file:
		lista_str = riga.split()

		for i in range(len(lista_str)):
			lista_str[i] = int(lista_str[i])

		lista_int = lista_str
		tupla = tuple(lista_int)
		lista.append(tupla)

	file.close()

	return lista


n = 1

lista = creazioneTriple(r"C:\Fond-Inf-Python\Risorse\Prove4txt")
lista_anni = []
dizionario = dict()

for tupla in lista:
	dizionario[tupla[2]] = dizionario.get(tupla[2], 0) + 1

for chiave in dizionario:
	if dizionario[chiave] > n:
		lista_anni.append(chiave)

print(dizionario)
print(lista_anni)