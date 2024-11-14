# Screivete programmi che leggano una riga di dati in ingresso sotto forma di stringa e visualizzino quanto segue:
# - le sole lettere masiucole della stringa
# - a partire dalla seconda lettera della stringa, una lettera viene visualizzata e l'altra no, alternativamente
# - la stringa, con tutte le vocali sostituite da un carattere di sttolineatura (underscore)
# - il numero di cifre presenti nella stringa
# - le posizioni di tutte le vocali presenti nella stringa


# Le sole lettere masiucole della stringa
stringa = input("Inserire una stringa: ")

stringa_min = stringa.lower()
risposta = ""

for i in range(0,len(stringa)):
    if stringa[i] != stringa_min[i]:
        risposta += stringa[i] + " "

# In alternativa:
for i in range(0,len(stringa)):
    if stringa[i].isupper():
        risposta += stringa[i] + " "

if risposta == "":
    print("Non ci sono lettere maiuscole nella stringa")
else:
    print(risposta)


# A partire dalla seconda lettera della stringa, una lettera viene visualizzata e l'altra no, alternativamente
stringa = input("Inserire una stringa: ")

risposta = ""

for i in range(1,len(stringa),2):
    risposta += stringa[i] + " "

print(risposta)


# La stringa, con tutte le vocali sostituite da un carattere di sttolineatura (underscore)
stringa = input("Inserire una stringa: ")

stringa = stringa.lower()

for i in range(0,len(stringa)):
    if stringa[i] == "a" or stringa[i] == "e" or stringa[i] == "i" or stringa[i] == "o" or stringa[i] == "u":
        stringa = stringa.replace(stringa[i],"_")

print(stringa)


# Il numero di cifre presenti nella stringa
stringa = input("Inserire una stringa: ")

numero_cifre = 0

for i in range(0,len(stringa)):
    if stringa[i].isdigit():
        numero_cifre += 1

print("Il numero di cifre presenti nella stringa è:", numero_cifre)


# Le posizioni di tutte le vocali presenti nella stringa
stringa = input("Inserire una stringa: ")
stringa = stringa.lower()

vocale_a = ""
vocale_e = ""
vocale_i = ""
vocale_o = ""
vocale_u = ""

for i in range(0,len(stringa)):
    if stringa[i] == "a":
        vocale_a += str(i+1) + " "  # str(i+1) poiché per python la prima posizone è data dal numero 0, per noi invece di solito dal numero 1
    elif stringa[i] == "e":
        vocale_e += str(i+1) + " "
    elif  stringa[i] == "i":
        vocale_i += str(i+1) + " "
    elif  stringa[i] == "o":
        vocale_o += str(i+1) + " "
    elif  stringa[i] == "u":
        vocale_u += str(i+1) + " "

print("la vocale a si trova in posizione",vocale_a)
print("la vocale e si trova in posizione",vocale_e)
print("la vocale i si trova in posizione",vocale_i)
print("la vocale o si trova in posizione",vocale_o)
print("la vocale u si trova in posizione",vocale_u)