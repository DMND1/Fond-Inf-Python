# In una lista, chiamiamo "serie" (run) una sequenza di valori adiacienti ripetuti. Scrivete un programma che generi una sequenza di 20 lanci casuali di un dado e 
# visualizzi i singoli risultati, racchiudendo le serie tra parentesi tonde per evidenziarle

def valoriAdiacienti():
    from random import randint
    inRun = False
    lista = []
    risultato = ""

    for i in range(20):
        lista.append(randint(1,6))

    for i in range(len(lista)-1):
        if inRun and lista[i] != lista[i-1]:
            risultato += ")"
            inRun = False
        if (not inRun) and lista[i] == lista[i+1]:
            risultato += "("
            inRun = True
        risultato += str(lista[i])
    if inRun:
        risultato += ")"
    
    return risultato


print(valoriAdiacienti())