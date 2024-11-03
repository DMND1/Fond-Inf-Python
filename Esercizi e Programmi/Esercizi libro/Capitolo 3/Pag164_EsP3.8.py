# Scrivete un programma che legga 4 numeri interi e visualizzi li messaggio "two pairs" se i dati acquisiti costituiscono due coppie (in qualisasi ordine)
#  e "not two pairs" in caso contrario. Ad esempio:
# 1 2 2 1   two pairs
# 1 2 2 3   not two pairs
# 2 2 2 2   two pairs

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))
n4 = float(input("Numero 4: "))

risultato = "not two pairs"

if (n1 == n2 and n3 == n4) or (n1 == n3 and n2 == n4) or (n1 == n4 and n2 == n3):
    risultato = "two pairs"

print(risultato)