lista = [5,3,4,2]

lista[1]    # stampa 3

lista[1:3]  # stampa [3,4]

i = 2
lista[1]    # stampa 4

for i in range(0,len(lista)):   # ciclo che da anche un valore all'indice
    print(i, lista[i])

for elemento in lista:          # ciclo se non serve il valore dell'indice
    print(elemento)

for elemento in lista:          # ciclo se non serve il valore dell'indice
    print(elemento, end=" ")    # sostituiamo l'istruzione finale di print con una stringa