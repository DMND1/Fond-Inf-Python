# ??? Probabilmente questo esercizio doveva essere del primo capitolo e non del terzo ???

# Scrivete un programma che legga tre numeri in virgola mobile e visualizzi il maggiore di essi, usando la funzione max. Ad esempio:
# Enter a number: 4
# Enter a number: 9
# Enter a number: 2.5
# The largest number is 9.0

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

massimo = max(n1, n2, n3)

print("Il numero più grande è:", massimo)