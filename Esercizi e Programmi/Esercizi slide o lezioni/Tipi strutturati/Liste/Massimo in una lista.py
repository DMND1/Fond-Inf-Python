# trovare il massimo elemento in li (senza usare la funzione max)
li = [1,2,3,4,56,5,4,3,2,1,88,11]

minimo = li[0]
massimo = li[0]

for i in li:
    if i < minimo:
        minimo = i
    elif i > massimo:
        massimo = i

print("Il massimo vale:", massimo)
print("Il minimo vale:", minimo)


# altrimenti sempre per trovare il massimo elemento in li (senza usare la funzione max)
li.sort()

print("Il massimo vale:", li[len(li)-1])
print("Il minimo vale:", li[0])