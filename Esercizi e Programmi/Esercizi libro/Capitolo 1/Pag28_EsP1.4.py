# Programma per visualizzare un conto bancario dopo 1, 2 e 3 anni, con interesse semplice annuo del 5% e un saldo iniziale di 1000 dollari $

saldo = 1000
saldo_1 = saldo + saldo * 5/100
saldo_2 = saldo_1 + saldo_1 * 5/100
saldo_3 = saldo_2 + saldo_2 * 5/100

print("Il saldo dopo un anno sarà: ", saldo_1)
print("Il saldo dopo due anni sarà: ", saldo_2)
print("Il saldo dopo tre anni sarà: ", saldo_3)