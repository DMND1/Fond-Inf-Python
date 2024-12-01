# Scrivete la funzione equals(a, b) che verifichi se due liste contengono gli stessi elementi nello stesso ordine
# Se la consegna intende di verificare che due liste siano uguali (? non capisco perché non si possa scrivere direttamente così in tal caso):

def equals(a, b):
    if len(a) != len(b):
        return False
    else:                       # Questo else è omissibile
        for i in range(len(a)):
            if a[i] != b [i]:
                return False
        return True