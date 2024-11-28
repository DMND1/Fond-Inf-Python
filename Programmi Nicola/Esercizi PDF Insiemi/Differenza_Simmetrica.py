a = {1,2,3,4}
b = {3,4,5,6}

ris = a.difference(b) #Ottengo gli elementi comuni di ogni insieme e li unisco
ris2 = b.difference(a)

risfin = ris.union(ris2)
print(risfin)