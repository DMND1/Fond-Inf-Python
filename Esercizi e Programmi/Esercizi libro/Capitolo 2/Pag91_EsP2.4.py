# Programma che chiede due interi all'utente e ne calcola: somma, diffrenza, prodotto, valore medio, distanza, valore massimo e minimo

x = int(input("Primo numero intero: "))
y = int(input("Secondo numero intero: "))

somma = x + y
diff = x - y
prod = x * y
val_med = somma/2
dist = abs(diff)
massimo = max(x,y)
minimo = min(x,y)

print("la somma vale:", somma)
print("la differenza vale:", diff)
print("il prodotto vale:", prod)
print("il valore medio vale:", val_med)
print("la distanza vale:", dist)
print("il massimo vale:", massimo)
print("il minimo vale:", minimo)