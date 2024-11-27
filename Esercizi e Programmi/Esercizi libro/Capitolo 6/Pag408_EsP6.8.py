# Scrivete un programma che calcoli la somma alternata degli elementi di una lista. se lista = [1, 2, 3, 4, 5, 4, 3, 2, 5], il programma deve calcolare 1 - 2 + 3 - 4 ...

lista = [1, 2, 3, 4, 5, 4, 3, 2, 5]
somma = 0

if lista == []:
    somma = None
else:
    for i in range(len(lista)):
        if i % 2 == 0:
            somma += lista[i]
        else:
            somma -= lista[i]

print(somma)