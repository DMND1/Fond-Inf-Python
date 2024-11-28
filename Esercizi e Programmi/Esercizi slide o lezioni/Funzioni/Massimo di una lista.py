def massimo(l): # restituisce il massimo del valori in l
    massimo = l[0]
    for i in l:
        if i > massimo:
            massimo = i
    
    return massimo

lista = [1,2,3,4,5]
print(massimo(lista))