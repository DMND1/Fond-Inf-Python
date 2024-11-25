# Due numeri sono coprimi se non hanno divisori in comune. Realizzare una funzione per controllare se due numeri sono coprimi.

# Trovare i divisori di un numero n1 e metterli in una lista
# Trovare i divisori di un numero n2 e metterli in una lista
# se c'è un elemento in comune tra le due liste (che non sia 1):
#   i due numeri non sono coprimi
# altrimenti:   (ossia se non ci sono divisori in comune)
#   i due numeri sono coprimi

def Coprimi(x1, x2):
    l1 = []
    l2 = []

    for i in range(2, x1+1):
        if x1 % i == 0:
            l1.append(i)
    
    for c in range(2, x2+1):
        if x2 % c == 0:
            l2.append(c)

    coprimi = True

    for i in l1:
        if i in l2:
            coprimi = False
            break

    return coprimi

print(Coprimi(14,15))   # Stampa True
print(Coprimi(14,2))    # Stampa False