# Due numeri sono coprimi se non hanno divisori in comune. Realizzare una funzione per controllare se due numeri sono coprimi.

# Trovare i divisori di un numero n1 e metterli in una lista
# Trovare i divisori di un numero n2 e metterli in una lista
# se c'è un elemento in comune tra le due liste (che non sia 1):
#   i due numeri non sono coprimi
# altrimenti:   (ossia se non ci sono divisori in comune)
#   i due numeri sono coprimi
from time import perf_counter


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

t1_start = perf_counter()
print(Coprimi(14,15))   # Stampa True
print(Coprimi(14,2))    # Stampa False
t1_stop = perf_counter()
print("Tempo di calcolo:", t1_stop - t1_start)


def Coprimi2(n, m):
    for i in range(2, min(m, n) + 1):
        if n % i == 0 and m % i == 0:
            return False
    return True

t1_start = perf_counter()
print(Coprimi2(14,15))   # Stampa True
print(Coprimi2(14,2))    # Stampa False
t1_stop = perf_counter()
print("Tempo di calcolo:", t1_stop - t1_start)


# Se i numeri non sono coprimi ritornare la lista dei fattori comuni
def Coprimi3(n, m):
    lista_fattori_comuni = []
    coprimi = True
    for i in range(2, min(n,m) + 1):
        if n % i == 0 and m % i == 0:
            lista_fattori_comuni.append(i)
            coprimi = False
    
    if coprimi:
        return True
    else:
        return lista_fattori_comuni

t1_start = perf_counter()
print(Coprimi3(14,15))   # Stampa True
print(Coprimi3(28,4))    # Stampa [2, 4]
t1_stop = perf_counter()
print("Tempo di calcolo:", t1_stop - t1_start)