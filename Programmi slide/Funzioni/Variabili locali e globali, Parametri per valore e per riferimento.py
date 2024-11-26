a = 1

def f(x):
    a = 3
    print(a, x)

f(5)        # Stampa: 3 5
print(a)    # Stampa: 1
print(x)    # Stampa: Errore, la x non esiste, non è definita


a = 1
lista = [1, 2, 0, 4, 5]
sequenza = [7.0, 1, "a", 3.0]

def g(l):       # Quando mettiamo al posto di l lista, stiamo assegnando a l il valore di lista, adesso l e lista sono la stessa lista
    l[2] = 3    # Per questo modificando l si modifica anche lista
    print(l)

print(lista)    # Stampa: [1, 2, 0, 4, 5]
print(sequenza) # Stampa: [7.0, 1, "a", 3.0]

g(lista)        # Stampa: [1, 2, 3, 4, 5]
g(sequenza)     # Stampa: [7.0, 1, 3, 3.0]

print(lista)    # Stampa: [1, 2, 3, 4, 5]
print(sequenza) # Stampa: [7.0, 1, 3, 3.0]