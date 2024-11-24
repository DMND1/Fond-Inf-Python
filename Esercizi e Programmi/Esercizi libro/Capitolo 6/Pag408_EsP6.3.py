# Scrivete un programma che inserisca in una lista tutti i numeri da 2 a 10000, poi elimini da tale lista i multipli di 2 (tranne 2), i multipli di 3 (tranne 3), 
# e così via, fino ai multipli di 100, visualizzando, infine, i valori rimasti nella lista

lista = []

for i in range(2,10001):
    lista.append(i)
print(lista, "\n")


for i in range(2,101):
    for c in lista:
        if c != i and c % i == 0:
            lista.remove(c)

print(lista)