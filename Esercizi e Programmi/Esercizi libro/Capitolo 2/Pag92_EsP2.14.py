# Scrivere un programma che legga un numero compreso tra 1000 e 999999, dopo averlo chiesto all'utente, per poi visualizzarlo con una virgola come separatore delle migliaia, 
# secondo l'uso anglosassone

x = " " + " " + " " + str(input("Inserire un numero compreso tra 1000 e 999999: "))


n = x[len(x)-6:len(x)-3] + "," + x[len(x)-3:len(x)]

print(n.replace(" ", ""))

# Veramente molto macchinosa come soluzione, spero ce ne sia una migliore e più semplice suggerita da voi ;)