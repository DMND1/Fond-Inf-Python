# In relazione al circuito qui raffigurato, scrivete un programma che acquisisca come dati in ingresso le resistenze dei tre resistori e calcoli la resistenza totale
# usando la legge di Ohm

R1 = float(input("Resistenza 1: "))
R2 = float(input("Resistenza 2: "))
R3 = float(input("Resistenza 3: "))

R_eq = R2 * R3 / (R2 + R3)  # Poiché 1 / R_eq = 1 / R1 + 1 / R2
R_tot = R1 + R_eq

print("La resistenza totale sarà:", R_tot)