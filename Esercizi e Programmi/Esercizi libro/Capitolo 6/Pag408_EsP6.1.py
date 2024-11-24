# Scrivete un programma che inizializzi una lista con dieci numeri interi casuali e, poi, visualizzi quattro righe di informazioni contenenti:
# - Tutti gli elementi di indice pari
# - Tutti gli elementi di valore pari
# - Tutti gli elementi in ordine inverso
# - Il primo e l'ultimo elemento

from random import randint

lista_originale = []

for i in range(10):
    lista_originale.append(randint(-1000,1000))

print(lista_originale)


# Tutti gli elementi di indice pari
lista_elem_pari = []

for i in range(0, len(lista_originale), 2):
    lista_elem_pari.append(lista_originale[i])

print(lista_elem_pari)


# Tutti gli elementi di valore pari
lista_pari = []

for i in lista_originale:
    if i % 2 == 0:
        lista_pari.append(i)

print(lista_pari)


# - Tutti gli elementi in ordine inverso
lista_inversa = []

for i in range(len(lista_originale) - 1, -1, -1):
    lista_inversa.append(lista_originale[i])

print(lista_inversa)


# - Il primo e l'ultimo elemento
print(lista_originale[0], lista_originale[-1])