# Una cartella per il gioco della tombola è rappresentata da un file testo contenente 15 interi, tra 1 e 90

# 1 23 44 61 80
# 16 26 59 68 89
# 28 49 58 71 84

# realizzare una funzione che, ricevendo come parametro il nome di un file-cartella, restitusca un dizionario di 3 elementi, le cui chiavi sono "riga 1",
# "riga 2", "riga 3" e come valore i primi cinque numeri, i successivi cinque e gli ultimi. chiamiamo tale dizionario "dizionario-cartella"

def creazioneDizionario(nome_file):
    dizionario = {}
    file = open(nome_file, "r")
    i = 1

    for riga in file:
        numeri_str = riga.strip()
        lista_numeri = numeri_str.split()

        for k in range(len(lista_numeri)):
            lista_numeri[k] = int(lista_numeri[k])

        dizionario["riga " + str(i)] = lista_numeri

        i += 1

    file.close()

    return dizionario

# realizzare una seconda funzione che presi come parametri un diozionario-cartella, una chiave k e una lista di numeri L, 
# restitusca quanti numeri associati alla chiave k del dizionario-cartella sono presenti in L

def controlloNumeri(dizionario, k, L):
    tutti_i_numeri = set(dizionario[k])
    numeri_da_controllare = set(L)
    interesezione = tutti_i_numeri.intersection(numeri_da_controllare)

    return len(interesezione)

# Fare lo stesso esercizio senza usare i set


# Progoramma
from random import randint

# nome_file =input("Nome file: ")
nome_file = "C:\Python\Fond-Inf-Python\Esercizi e Programmi\Esercizi slide o lezioni\Esercitazioni prova esonero\\Numeri tombola.txt"
dizionario_cartella = creazioneDizionario(nome_file)

lista_estratti = []

while len(lista_estratti) < 30:
    numero = randint(1, 90)
    if numero not in lista_estratti:
        lista_estratti.append(numero)

print(lista_estratti, len(lista_estratti))

numeri_segnati_1 = controlloNumeri(dizionario_cartella, "riga 1", lista_estratti)
numeri_segnati_2 = controlloNumeri(dizionario_cartella, "riga 2", lista_estratti)
numeri_segnati_3 = controlloNumeri(dizionario_cartella, "riga 3", lista_estratti)

somma_estratti = numeri_segnati_1 + numeri_segnati_2 + numeri_segnati_3 

if somma_estratti == 15:
    print("Tombola")
else:
    print("Buon Natale")