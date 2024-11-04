# Scrivete un programma che traduca un muero compreso tra 0 e 4 nel voto letterale più vicino. Ad esempio, il numero 2.8 deve essere tradotto in B-. 
# Risolvete i casi di parità in favore del voto maggiore: ad esmpio 2.85 deve essere tradotto come B

n = float(input("Numero (tra 0 e 4) da convertire in voto: "))

# A = 4.0
# A- = 3.7
# B+ = 3.3
# B = 3.0
# B- = 2.7
# C+ = 2.3
# C = 2.0
# C- = 1.7
# D+ = 1.3
# D = 1.0
# D- = 0.7
# F = 0

if n < 0 or n > 4:
    print("Errore: immetere un numero compreso tra 0 e 4")
else:
    if n >= 3.85:
        risultato = "A"
    elif 3.5 <= n < 3.85:
        risultato = "A-"
    elif 3.15 <= n < 3.5:
        risultato = "B+"
    elif 2.85 <= n < 3.15:
        risultato = "B"
    elif 2.5 <= n < 2.85:
        risultato = "B-"
    elif 2.15 <= n < 2.5:
        risultato = "C+"
    elif 1.85 <= n < 2.15:
        risultato = "C"
    elif 1.5 <= n < 1.85:
        risultato = "C-"
    elif 1.15 <= n < 1.5:
        risultato = "D+"
    elif 0.85 <= n < 1.15:
        risultato = "D"
    elif 0.5 <= n < 0.85:
        risultato = "D-"
    else:
        risultato = "F"
    
    print("Il voto equivalente è:", risultato)