# Realizzare una funzione che ricevendo in ingresso un naturale e una base lo scriva in quella base

def CambioDiBase(n, base):
    quoziente = n // base
    resto = n % base

    risultato = str(resto)     # Ultima cifra

    while quoziente != 0 :
        resto_numero = quoziente % base
        risultato = str(resto_numero) + risultato
        quoziente = quoziente // base
    
    return(risultato)

print(CambioDiBase(3,2))    # stampa 11 che è 3 in binario