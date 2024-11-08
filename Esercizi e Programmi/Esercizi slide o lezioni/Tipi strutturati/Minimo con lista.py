lista = [5,3,4,2]

# per tutti gli elementi calcolo la loro somma
# calcolo il numero degli elementi con len(lista)

minimo = lista[0]

for elemento in lista:
    if elemento < minimo:
        minimo= elemento

print("Minimo: ", minimo)

# ciclo con indice, che salta il primo "controllo"
for i in range(1,len(lista)):
    if lista[i] < minimo:
        minimo = lista[i]

# O in alternativa Xd:
print("Minimo: ", min(lista))