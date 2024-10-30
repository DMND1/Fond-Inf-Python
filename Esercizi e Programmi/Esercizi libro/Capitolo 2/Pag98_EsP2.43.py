# In base alla Legge di Coulomb, la forza electrica tra due particelle elettncamente cariche con carica pari a QI e Q2 Coulomb e poste a una distanza di r metri, 
# é uguale F = Q1 * Q2 / (4 * pi * epsilon * r **2), dove epsilon = 8.854e-12 F/m. Scrivete un programma che calcoli e visualizzi la forza agente su una coppia di 
# particelle cariche, basandosi sui dati acquisiti dall'utente: Q1 Coulomb, Q2 Coulomb e r metri.

from math import pi

epsilon = 8.854e-12     # F/m

Q1 = float(input("Carica particella 1 (in Coulomb): "))
Q2 = float(input("Carica particella 2 (in Coulomb): "))
r = float(input("Raggio (in metri): "))

F = Q1 * Q2 / (4 * pi * epsilon * r **2)
F = round(F, 2)

print("La forza agente sulla coppia di particelle cariche vale:", F, "N")