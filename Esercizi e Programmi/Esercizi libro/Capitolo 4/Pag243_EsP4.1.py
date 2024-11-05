# Scrivete programmi che usando cicli calcolino quanto segue:

# - la somma di tutti i numeri pari compresi tra 2 e 100 (estremi esclusi)
# - la somma di tuti i numeri compresi tra 1 e 100 (estremi esclusi) che siano quadrati perfetti
# - tutte le potenze di 2, da 2**0 a 2**20
# - la somma di tutti i numeri dispari compresi tra a e b (estremi esclusi), dove a e b sono valori acquisiti in ingresso
# - la somma di tutte le cifre dispari di un numero acquisito in ingresso (se ad esempio, il numero è 32677, la somma da calcolare è 3 + 7 + 7 = 17)


# La somma di tutti i numeri pari compresi tra 2 e 100 (estremi esclusi)
somma = 0
for i in range(4,100,2):
    somma += i

print(somma)


# La somma di tuti i numeri compresi tra 1 e 100 (estremi esclusi) che siano quadrati perfetti
from math import sqrt

somma = 0
for i in range(2,100):
    if int(sqrt(i))**2 == i:
        somma += i

print(somma)


# Tutte le potenze di 2, da 2**0 a 2**20
for i in range(0,21):
    print(2**i)


# La somma di tutti i numeri dispari compresi tra a e b (estremi esclusi), dove a e b sono valori acquisiti in ingresso

# non viene specificato se a e b sono interi, se non lo dovessero essere, poiché i numeri dispari e pari sono definiti solo per interi, basta scrivere:
# a = int(float(input("Numero a: ")))
# b = int(float(input("Numero b: ")))

# Pseudocodice:
# a è pari o dispari? :
#   se a % 2 == 0:
#       a è pari : poni a + 1 come primo estremo del ciclo for
#   altrimenti:
#       a è dispari : poni a + 2 come primo estremo del ciclo for
# b è pari o dispari?
#   se b % 2 == 0:
#       b è pari : poni b come secondo estremo del ciclo for
#   altrimenti:
#       b è dispari : poni b - 2 come secondo estremo del ciclo for

# il ciclo parte da a + 1 o a + 2 e deve terminare al numero dispari precedente a b

# il ciclo deve avere passo 2, poiché inizierà sempre da un numero dispari, che addizionato a 2 da un'altro numero dispari:

# Prima implementazione:
a = int(float(input("Numero a: ")))
b = int(float(input("Numero b: ")))

if a % 2 == 0:
    estremo1 = a + 1
else:
    estremo1 = a + 2

if b % 2 == 0:
    estremo2 = b
else:
    estremo2 = b - 2

somma = 0
for i in range(estremo1, estremo2, 2):
    somma += i

print(somma)

# volendo si possono mettere gli if dentro il ciclo for:
# Seconda implementazione:
somma = 0
for i in range(a+1,b):
    if i % 2 != 0:
        somma += i

print(somma)

# In teoria la prima soluzione è quella più lunga (per scrittura) ma che permette a python di fare meno operazioni possibili rispetto alla seconda, ed è quindi la più efficiente


# La somma di tutte le cifre dispari di un numero acquisito in ingresso (se ad esempio, il numero è 32677, la somma da calcolare è 3 + 7 + 7 = 17)

n = float(input("Numero: "))

n = str(n)              # rendo n una stringa
n = n.replace(".", "")  # tolgo un eventuale punto (virgola)

# si osservi che li eventuali 0 dopo la virgola non influenzano l'esecuzione del programma

somma = 0
for i in range(0,len(n)):
    cifra = int(n[i])
    if cifra % 2 != 0:
        somma += cifra

print(somma)