# Data una lista, eliminare gli elementi che appaiono due volte o più

lista = [1,2,3,4,5,5,2]

def removeDuplicates(lista):
    lista = set(lista)
    lista = list(lista)
    return lista

print(removeDuplicates(lista))