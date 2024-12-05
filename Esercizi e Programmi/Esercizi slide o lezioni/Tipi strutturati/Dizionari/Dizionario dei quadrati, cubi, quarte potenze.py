# Creare un dizionario D le cui chiavi sono i naturali fino a 100 e ogni valore è una lista contenente il quadrato, il cubo, e la quarta potenza della chiave

D = {}

for n in range(1,101):
    D[n] = [n ** 2, n ** 3, n ** 4]

print(D)



# Stampare il dizionario D sotto forma di tabella in cui ogni riga contiene la chiave e i valori della lista associata
for elem in D:
    risultato = ""
    for numero in D[elem]:
        risultato += str(numero) + ", "
    # Rimuovo lo spazio e la virgola finali
    risultato = risultato[:len(risultato)- 2]
    print(str(elem) + ": "+ risultato)



# Dato il dizionario D, chiedere all’utente un numero n e dire se n è un quadrato, cubo o quarta potenza di un numero minore di 100.

# Se vogliamo solo verificare se sia un quadrato o un cubo o una quata potenza ma senza dire di quale numero
n = int(input("Inserire un numero: "))

def presente(dizionario, n):
    for elem in dizionario:
        for numero in dizionario[elem]:
            if n == numero:
                return True
    
    return False

if presente(D, n):
    print("Il numero", n, "è un quadrato o un cubo o una quarta potenza di un numero minore di 100")
else:
    print("Il numero", n, "non è né un quadrato né un cubo né una quarta potenza di un numero minore di 100")


# Altrimenti se vogliamo dire di quale numero minore di 100 ne è il quadrato o cubo o la quarta potenza
n = int(input("Inserire un numero: "))
numero_trovato = False

for elem in D:
    for numero in D[elem]:
        if n == numero:
            numero_trovato = True
            chiave = elem

if numero_trovato:
    if n == 1:
        print("Il numero", n, "è il quadrato, il cubo e la quarta potenza di se stesso")
    elif D[chiave][0] == n:
        print("Il numero", n, "è il quadrato del numero", chiave)
    elif D[chiave][1] == n:
        print("Il numero", n, "è il cubo del numero", chiave)
    elif D[chiave][2] == n:
        print("Il numero", n, "è la quarta potenza del numero", chiave)
else:
    print("Il numero", n, "non è né un quadrato né un cubo né una quarta potenza di un numero minore di 100")