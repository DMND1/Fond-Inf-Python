# Scrivete la funzione: def countVowel(string)
# che restituisca il numero di vocali presenti nella stringa string. Le vocali sono le lettere a, e, i, o, u, y, oltre alle rispettive masiucole

def countVowel(string):
    string = string.lower()
    vocali = "aeiouy"
    contiene_vocali = False
    for i in string:
        if i in vocali:
            contiene_vocali = True
            break
    
    return contiene_vocali

print(countVowel("CiaO"))   # Stampa True
print(countVowel("Dpsx"))   # Stampa False