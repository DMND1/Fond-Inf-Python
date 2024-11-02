# scrivere un programma che legga un numero intero di 5 cifre
# tale numero lo deve stampare con uno spazio in mezzo a tutte le cifre

n = int(input("Numero di 5 cifre: "))

n_str = str(n)

print(n_str[0], n_str[1], n_str[2], n_str[3], n_str[4])

# risolvere lo stesso esercizio senza passare per le stringhe

cifra1 = int(n/(10**4))
cifra2 = int(n/(10**3)) - cifra1*10
cifra3 = int(n/(10**2)) - cifra1*10**2 - cifra2*10
cifra4 = int(n/(10**1)) - cifra1*10**3 - cifra2*10**2 - cifra3*10
cifra5 = int(n/(10**0)) - cifra1*10**4 - cifra2*10**3 - cifra3*10**2 - cifra4*10

print(cifra1, cifra2, cifra3, cifra4, cifra5)
# Questa soluzoine potrebbe avere problemi, pes esempio 4.35 * 100 = 434.99999999999994



# soulzione professore

# In alternativa: 
# Oss:
# 17294 // 10 = 1729 = q1
# 17294 % 10 = 4 = r1

q1 = n // 10
r1 = n % 10

q2 = q1 // 10
r2 = q1 % 10

q3 = q2 // 10
r3 = q2 % 10

q4 = q3 // 10
r4 = q3 % 10

q5 = q4 // 10
r5 = q4 % 10

print(r5, " ", r4, " ", r3, " ", r2, " ", r1)
print(r5, r4, r3, r2, r1)