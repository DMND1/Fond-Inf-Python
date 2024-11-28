def conversione(n,b):
    q = n // b
    r = n % b
    ris = str(r)
    while q != 0:
        r = q % b
        ris = str(r) + ris
        q = q // b
    return ris

#programma principale

n = int(input("Inserisci un numero da convertire: "))
b = int(input("Scegli una base da 2 a 16 con cui convertire il numero: "))

number = conversione(n,b)
print(number)

    