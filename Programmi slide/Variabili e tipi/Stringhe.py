#Una stringa vuota del tipo "" ha valore 0

#L'istruzione print può prendere una sezione di elementi separati da virgole:

print("Ciao a tutti",28,5.432,"Stringa")

#Quando si fa la somma di due interi 1 + 1, la somma non è uguale alla somma tra stringhe "1"+"1"

# con "len()" posso controllare la lunghezza di una stringa, ovviamente se eseguo il comando su una stringa vuota
# la stringa avrà valore 0

# nelle operazioni tra stringhe, l'operatore "+" diventa un concatenatore.

nome = "Gabriele"
cognome = "D'Annunzio"

print(nome + " "+ cognome)

#l'operatore "*" nelle stringhe si pone come ripetitore

trattino = "-"
trattino30 = trattino * 30

#Non si possono sommare una stringa o un intero, il compilatore non capisce se deve applicare la somma o la concatenazione!
#Stessa cosa vale per il ripetitore "*"
# L'operatore "=" serve ad assegnare un valore, l'operatore "==" si usa per confrontare due valori.
# nei confronti, il calcolatore risponderà secondo l'algebra booleana.

#Il comportamento di una stringa viene definito dai suoi metodi:

filosofo = "AristoTele"

print(filosofo.upper) #stampa la variabile filosofo in uppercase
print(filosofo.lower) #stampa la variabile filosofo in lowercase

filosofo_2 = filosofo.replace("AristoTele","Socrate") #sostituisce il contenuto della stringa

#data una stringa, quest ultima è indicizzata, ossia che ogni carattere presenta un indice a partire da 0

v = "ciao"

vars = v[2] #usando la simbologia [x:y] si vanno a stampare gli indici che partono da x a y, y escluso

#Scriviamo un programma che, inserita una stringa, stampi la stringa col primo carattere in maiuscolo

print("inserisci il nome")

x = input()

x = x.lower()

nuovon = x[0].upper() + x[1:len(x)]

print(nuovon)