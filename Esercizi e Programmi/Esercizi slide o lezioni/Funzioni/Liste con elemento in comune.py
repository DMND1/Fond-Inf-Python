# Realizzare una funzione che ricevendo due liste in ingresso controlli se abbiano o meno un elemento in comune

l1 = ["gli", "i", "il", "la", "le", "lo","Napoli"]
l2 = [1,2,3,4,5,8,11,"gli"]

elem_comune = False

for i in l1:
    if i in l2:
        elem_comune = True
        break

print(elem_comune)  # stampa True


l1 = ["gli", "i", "il", "la", "le", "lo","Napoli"]
l2 = [1,2,3,4,5,8,11]

elem_comune = False

for i in l1:
    if i in l2:
        elem_comune = True
        break

print(elem_comune)  # stampa False