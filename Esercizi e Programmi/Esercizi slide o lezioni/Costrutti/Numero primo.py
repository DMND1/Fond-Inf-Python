# Verificare se un numero è primo o no
# Programma professore:
# leggi n
# trovato = False
# per tutti gli i da 2 a n-1:
#   se i divide n con resto 0 ho trovato un divisore intero:
#       trovato = True

n = int(input("Inserire un numero naturale: "))

trovato_divisore = False

for i in range(2,n):
    if n % i == 0:
        trovato_divisore = True

if trovato_divisore:
    print(n, " non è primo")
else:
    print(n, " è primo")



# Divisori di un numero

from math import sqrt

n = int(input("Inserire un numero naturale: "))
l = []

trovato_divisore = False

# Serve trovare tutti i divisori fino alla radice di n perché per ogni divisore prima di tale radice c'è un altro divisore dopo la radice, 
# il prododtto di questi due divisori è il numero n
for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
        trovato_divisore = True
        l.append(i)

if trovato_divisore:
    print(n, " non è primo")
else:
    print(n, " è primo")

print("Divisori: ", l)


# Stampare tutt i numeri primi prima di n
n = int(input("Inserire un numero naturale: "))

for m in range(2,n+1):
    trovato_divisore = False
    for i in range(2, int(sqrt(m))+1):
        if m % i == 0:
            trovato_divisore = True

    if not trovato_divisore:
        print(m)