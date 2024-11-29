# Creazione dell'insieme di tutte le letter dell'alfabeto

alfabeto = set()
c = "a"
while ord(c) <= ord("z"):
    alfabeto.add(c)
    c = chr(ord(c) + 1)


# Chiedere all’utente una frase e verificare se contiene tutte le lettere dell’alfabeto.
frase = input("Inserire una frase: ")

def tutteLettereAlfabeto(stringa):
    stringa = stringa.lower()

    alfabeto = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

    lettere = set(stringa)

    if alfabeto.issubset(lettere):
        return True
    else:
        return False


# In alternativa:
frase = input("Inserire una frase: ")
print(tutteLettereAlfabeto(frase))

frase = frase.lower()
frase = frase.replace(" ", "")

alfabeto = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

contiene_tutte = True

for lettera in alfabeto:
    if lettera not in frase:
        contiene_tutte = False

if contiene_tutte:
    print("La frase contiene tutte le lettere dell'alfabeto")
else:
    print("La frase non contiene tutte le lettere dell'alfabeto")