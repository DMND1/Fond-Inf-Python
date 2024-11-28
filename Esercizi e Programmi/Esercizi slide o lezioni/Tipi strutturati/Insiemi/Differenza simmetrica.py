# Dati due insiemi calcolare la differenza simmetrica, cioè l’insieme degli elementi presenti solo in uno dei due insiemi

insieme1 = {1,2,3,4,5,6}
insieme2 = {3,4,5,6,7}

def diffSimm(insieme1, insieme2):
    intersezione = insieme1.intersection(insieme2)

    risultato1 = insieme1.difference(intersezione)
    risultato2 = insieme2.difference(intersezione)

    risultato = risultato1.union(risultato2)

    return risultato

print(diffSimm(insieme1, insieme2))