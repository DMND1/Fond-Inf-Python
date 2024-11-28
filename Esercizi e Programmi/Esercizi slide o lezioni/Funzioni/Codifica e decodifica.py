def codifica1(s, k):
    risultato = ""
    
    for l in s:
        l1 = chr(ord(l) + k)
        risultato += l1

    return risultato

print(codifica1("abc", 3))    # Stampa: def
print(codifica1("xyz", 3))    # Stampa: {|}


def decodifica1(s, k):
    risultato = ""
    
    for l in s:
        l1 = chr(ord(l) - k)
        risultato += l1

    return risultato


messaggio = input("Messaggio: ")
chiave = int(input("Chiave: "))

trasmesso = codifica1(messaggio, chiave)
print("Ho trasmesso:", trasmesso)

ricevuto = decodifica1(trasmesso, chiave)
print("Ho ricevuto", ricevuto)



"""
def codifica(s, k): # codifica una stringa s con chiave k
    s = s.lower()
    s_codificata = ""

    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for indice_lettera in range(len(s)):
        indice_lettera_alfabeto = alfabeto.index(s[indice_lettera])

        indice_codifica = indice_lettera_alfabeto + k

        if indice_codifica >= len(alfabeto):
            indice_codifica -= len(alfabeto)
    
        s_codificata += alfabeto[indice_codifica]

    return s_codificata

print(codifica("abc", 3))    # Stampa: def
print(codifica("xyz", 3))    # Stampa: abc


def decodifica(s, k): # decodifica la stringa s con chiave k
    s = s.lower()
    s_decodificata = ""

    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for lettera in range(len(s)):
        ...
"""

# Per una sola parola, e una chiave k
# sostituire una lettera con la sua successiva di k passi, se si va oltre 26 bisonga riniziare a contare dalla prima lettera dell'alfabeto

def codifica2(s, k):
    risultato = ""

    chiave = k % 26

    for l in s:
        l1 = chr(ord(l) + chiave)
        risultato += l1

    return risultato


print(codifica2("abc", 3))    # Stampa: def
print(codifica2("xyz", 3))    # Stampa: {|}


def decodifica1(s, k):
    risultato = ""
    
    chiave = k % 26

    for l in s:
        l1 = chr(ord(l) - chiave)
        risultato += l1

    return risultato