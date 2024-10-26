# Programma che chiede due interi all'utente e ne calcola: somma, diffrenza, prodotto, valore medio, distanza, valore massimo e minimo
# Fare in modo che la stampa sia come sul libro

x = int(input("Primo numero intero: "))
y = int(input("Secondo numero intero: "))

somma = x + y
diff = x - y
prod = x * y
val_med = somma/2
dist = abs(diff)
massimo = max(x,y)
minimo = min(x,y)


frase1 = "la somma vale:"
frase2 = "la differenza vale:"
frase3 = "il prodotto vale:"
frase4 = "il valore medio vale:"
frase5 = "la distanza vale:"
frase6 = "il massimo vale:"
frase7 = "il minimo vale:"


print(frase1, (len(frase4)-len(frase1))* " ", somma)
print(frase2, (len(frase4)-len(frase2))* " ", diff)
print(frase3, (len(frase4)-len(frase3))* " ", prod)
print(frase4, "", val_med)
print(frase5, (len(frase4)-len(frase5))* " ", dist)
print(frase6, (len(frase4)-len(frase6))* " ", massimo)
print(frase7, (len(frase4)-len(frase7))* " ", minimo)

# Programma da finire, le colonne non sono perfettamente allineate, i.e. la colonna delle unità, delle decine ecc.