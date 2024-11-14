# Controllare se in li ci sono elementi ripetuti
li = [1,2,3,4,56,5,4,3,2,1,88,11]

ripetuti = False

for i in range(len(li)):
    for c in range(len(li)):
        # Se trovo un numero che è uguale ad un'altro numero nella stessa lista ma che non ha lo stesso indice
        if li[i] == li[c] and i != c:
            # Ho trovato un elemento ripetuto
            ripetuti = True

print(ripetuti) # stampa True

# Lo stesso programma ma con una lista senza ripetizioni
li = [1,2,3,4,56,5,88,11]

ripetuti = False

for i in range(len(li)):
    for c in range(len(li)):
        # Se trovo un numero che è uguale ad un'altro numero nella stessa lista ma che non ha lo stesso indice
        if li[i] == li[c] and i != c:
            # Ho trovato un elemento ripetuto
            ripetuti = True

print(ripetuti) # stampa False