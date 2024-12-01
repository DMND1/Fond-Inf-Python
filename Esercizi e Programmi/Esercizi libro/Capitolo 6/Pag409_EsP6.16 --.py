# Scrivete un programma che generi una sequenza di 20 lanci casuali di un dado e visualizzi i singoli risultati, racchiudendo la serie più lunga tra parentesi tonde

# Da finire...

def seriePiùLunga():
    from random import randint
    lista = []
    risultato = ""
    contatore_max = 1

    for i in range(20):
        lista.append(randint(1,6))

        if lista[i] == lista[i-1] and i != 0:
            contatore += 2
            if contatore > contatore_max:
                contatore_max = contatore
                indice_numero = i
        else:
            contatore = 0

    print(indice_numero)
    print(contatore_max)
    print(lista)

    for c in range(contatore_max - 1):
        lista.pop(indice_numero - contatore_max + 1)

    print(lista)

    for i in range(len(lista)):
        if i == (indice_numero - contatore_max + 1):
            risultato += "(" + str(lista[i + 1]) * contatore + ")"
        else:
            risultato += " " + str(lista[i]) + " "

    return risultato


print(seriePiùLunga())