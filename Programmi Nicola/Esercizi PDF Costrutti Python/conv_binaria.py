#realizzare un programma che converta un numero in binario

num = int(input("inserisci un numero intero"))
while num > 0:
    quoziente = num%2
    bin = str(quoziente) + bin
    num = num/2

print(bin)

