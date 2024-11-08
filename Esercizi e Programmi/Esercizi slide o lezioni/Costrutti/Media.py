somma = 0
cont = 0
b = False

while b != True:
    num = int(input("Inserire un numero: "))
    if num  == 0:
        b = True
    else:
        somma = somma + num
        cont += 1

media = somma / cont
print("La media dei numeri inseriti è:", media)


# O in alternativa:
somma = 0
cont = 0

num = int(input("Inserire un numero: "))

if num == 0:
    print("Non si può calcolare la media")
    while num != 0:
        somma = somma + num
        cont += 1
        num = int(input("Inserire un numero: "))

    media = somma / cont
    print("La media dei numeri inseriti è:", media)


# O in alternativa:
somma = 0
cont = 0

n_str = input("Inserire un numero: ")

if n_str == "stop":
    print("Errore")
else:
    while n_str != "stop":
        n = int(n_str)
        somma = somma + num
        cont += 1
        n_str = input("Inserire un numero: ")

media = somma / cont
print("La media dei numeri inseriti è:", media)