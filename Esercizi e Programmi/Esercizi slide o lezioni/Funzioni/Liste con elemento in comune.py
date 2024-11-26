# Realizzare una funzione che ricevendo due liste in ingresso controlli se abbiano o meno un elemento in comune

l1 = ["gli", "i", "il", "la", "le", "lo","Napoli"]
l2 = [1,2,3,4,5,8,11,"gli"]

def ElemComune(l1, l2):
    
    for i in l1:
        if i in l2:
            return True
    
    return False

print(ElemComune(l1, l2))  # stampa True


l1 = ["gli", "i", "il", "la", "le", "lo","Napoli"]
l2 = [1,2,3,4,5,8,11]

print(ElemComune(l1, l2))  # stampa False