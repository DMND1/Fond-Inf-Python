# Raccogliere in una lista tutti gli elementi di li minori di 10
li = [1,2,3,4,56,5,4,3,2,1,88,11]
lista = []

for i in li:
    if i < 10:
        lista.append(i)

print("La lista che contiene tutti gli elementi di li minori di 10 è:", lista)