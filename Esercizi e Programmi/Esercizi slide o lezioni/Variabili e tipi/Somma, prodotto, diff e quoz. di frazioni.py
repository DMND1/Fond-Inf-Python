# Fare la somma, il prodotto, la differenza e il quoziente di due frazioni, con input utente

n1 = int(input("Numeratore prima frazione:"))
d1 = int(input("Denominatore prima frazione:"))
n2 = int(input("Numeratore seconda frazione:"))
d2 = int(input("Denominatore seconda frazione:"))

print("le due frazioni sono:", n1, "/", d1, " e ", n1, "/", d2)

# Addizione

n3 = n1*d2 + n2*d1
d3 = d1*d2

print(n1, "/", d1, " + ", n2, "/", d2, " = ", n3, "/", d3, " = ", n3 / d3)

# Sottrazione

n3 = n1*d2 - n2*d1
d3 = d1*d2

print(n1, "/", d1, " - ", n2, "/", d2, " = ", n3, "/", d3, " = ", n3 / d3)

# Prodotto

n3 = n1*n2
d3 = d1*d2

print(n1, "/", d1, " * ", n2, "/", d2, " = ", n3, "/", d3, " = ", n3 / d3)

# Quoziente

n3 = n1*d2
d3 = d1*n2

print(n1, "/", d1, " / ", n2, "/", d2, " = ", n3, "/", d3, " = ", n3 / d3)
