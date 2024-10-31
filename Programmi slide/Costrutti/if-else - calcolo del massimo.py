m = int(input ("Primo numero :"))
n = int(input("Secondo numero:"))

if m > n :
    max = m

else:   # Che in questo caso coincide con m <= n (m minore o ugale a n)
    max = n

print("Valore massimo:", max)