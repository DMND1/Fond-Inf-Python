# Scrivete funzioni che risolvano i problemi seguenti per liste di numeri interi, fornendo un programma di collaudo per ciascuna funzione:

# Scambiare tra loro il primo e l'ultimo elemento della lista
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def ScambioPrimoUltimo(lista):
    primo = lista[0]
    lista.pop(0)
    lista.insert(0, lista[-1])
    lista.pop(len(lista)-1)
    lista.append(primo)
    return lista

print(lista)                                           # Stampa [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]
print(ScambioPrimoUltimo(lista), end = "\n" + "\n")    # Stampa [5, 2, 3, 4, 56, 5, 4, 3, 2, 1]

# O in alternativa: Scambiare tra loro il primo e l'ultimo elemento della lista

def ScambioPrimoUltimo(lista):
    primo = lista[0]
    lista.insert(0, lista[-1])
    lista.pop(len(lista)-1)
    lista.pop(1)
    lista.append(primo)
    return lista

# Far scorrere tutti gli elementi di una posizione "verso destra", spostando l'ultimo elmento nella prima posizione
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def ScorrereLista(lista):
    lista.insert(0, lista[-1])
    lista.pop(len(lista)-1)
    return lista

print(lista)
print(ScorrereLista(lista), end = "\n" + "\n")


# Sostituire con 0 tuttli gli elementi pari
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def SostituzioneElemPari(lista):
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0:
            lista.pop(i)
            lista.insert(i, 0)
    return lista

print(lista)
print(SostituzioneElemPari(lista), end = "\n" + "\n")


# Sostituire ciascun elemento, tranne il primo e l'ultimo, con il più grande dei due elementi adiacienti
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def SostituzioneElemAdiaciente(lista):
    risultato = []
    risultato.append(lista[0])

    for i in range(1,len(lista)-1):
        risultato.append(max(lista[i-1], lista[i+1]))

    risultato.append(lista[-1])
    return risultato

print(lista)
print(SostituzioneElemAdiaciente(lista), end = "\n" + "\n")


# Eliminare l'elemento centrale della lista se questa ha dimensione dispari, altrimenti eliminare i due elementi centrali
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def EliminareElemCentrale(lista):
    if len(lista) % 2 == 0:
        estremo = len(lista) // 2 - 1
        lista.pop(estremo)
        lista.pop(estremo)
        return lista
    else:
        estremo = len(lista) // 2
        lista.pop(estremo)
        return lista

print(lista)
print(EliminareElemCentrale(lista), end = "\n" + "\n")

lista = [1, 2, 3, 4, 56, 5, 4, 3, 2]
print(lista)
print(EliminareElemCentrale(lista), end = "\n" + "\n")


# Spostare tutti gli elementi pari all'inizio della lsita, preservando però l'ordinamento relativo tra gli elementi, se si esclude la condizione posta
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def SpostareElemPari(lista):
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            var = lista[i]
            lista.pop(i)
            lista = [var] + lista
    return lista

print(lista)
print(SpostareElemPari(lista), end = "\n" + "\n")


# Restituire il secondo valore maggiore della lista
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def SecondoValoreMaggiore(lista):
    if len(lista) < 2:
        return "Input non valido"
    else:
        lista.sort()
        return lista[len(lista)-2]

print(lista)
print(SecondoValoreMaggiore(lista))

lista = [1]
print(lista)
print(SecondoValoreMaggiore(lista), end = "\n" + "\n")


# Restituire il secondo valore maggiore della lista (senza sort)
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def SecondoValoreMaggiore2(lista):
    lista.remove(max(lista))
    return max(lista)

print(lista)
print(SecondoValoreMaggiore2(lista), end = "\n" + "\n")


# Restituire True se e solo se la lista è ordina in ordine crescente
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def OrdinataCrescente(lista):
    lista_originale = list(lista)
    lista.sort()
    if lista_originale == lista:
        return True
    else:
        return False

print(lista)
print(OrdinataCrescente(lista), end = "\n" + "\n")

lista = [1, 2, 3, 4]
print(lista)
print(OrdinataCrescente(lista), end = "\n" + "\n")


# Restituire True se e solo se la lista contiene due elementi adiacienti duplicati
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def ElemAdiacientiDuplicati(lista):
    for i in range(0,len(lista)):
        if i == 0 and lista[i] == lista[i+1]:
            return True
        elif i != (len(lista)-1) and lista[i] == lista[i+1] or lista[i] == lista[i-1]:
            return True
        elif i == (len(lista)-1) and lista[i] == lista[i-1]:
            return True
    return False

print(lista)
print(ElemAdiacientiDuplicati(lista), end = "\n" + "\n")

lista = [1, 2, 3, 4, 56, 5, 4, 4, 2, 5]
print(lista)
print(ElemAdiacientiDuplicati(lista), end = "\n" + "\n")


# Restituire True se e solo se la lista contiene elementi duplicati (non necessariamente adiacienti)
lista = [1, 2, 3, 4, 56, 5, 4, 3, 2, 5]

def ElemeDuplicati(lista):
    for i in lista:
        var = i
        lista.remove(i)
        if var in lista:
            return True
    return False

print(lista)
print(ElemeDuplicati(lista), end = "\n" + "\n")

lista = [1, 2, 3, 4]
print(lista)
print(ElemeDuplicati(lista), end = "\n" + "\n")