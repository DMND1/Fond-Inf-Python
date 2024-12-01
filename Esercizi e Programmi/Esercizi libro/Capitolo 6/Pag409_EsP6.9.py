# Scrivete la funzione che inverta la sequenza degli elementi di una lista

def inversaLista(lista):
    lista_inversa = []
    for i in range(len(lista) - 1, -1, -1):
        lista_inversa.append(lista[i])
    
    return lista_inversa

lista = [1, 2, 3, 4, 5, 4, 3, 2, 5]

print(lista)
print(inversaLista(lista))