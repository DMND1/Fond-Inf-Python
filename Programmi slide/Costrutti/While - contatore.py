n = int(input("Numero: "))

cont = 0

while cont <= n :
    print(cont)
    cont = cont + 1

# il calcolatore per un numero di 3 cirfre impiega un tempo x per stampare tutti i numeri da 0 a quel numero
# per un numero di 4 cifre impiega un tempo 10x

# Il programma scritto così continua all'infinito
while cont != -1 :
    print(cont)
    cont = cont + 1

# Poiché cont != -1 vale True sempre si può scrivere anche così:
while True :
    print(cont)
    cont = cont + 1