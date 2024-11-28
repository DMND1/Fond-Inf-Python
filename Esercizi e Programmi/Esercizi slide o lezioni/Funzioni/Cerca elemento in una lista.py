def cerca(l, e): # risponde True se e è in l, False altrimenti
    for i in l:
        if i == e:
            return True
    
    return False

lista = [1,2,3,4,5]

print(cerca(lista, 3))
print(cerca(lista, 7))