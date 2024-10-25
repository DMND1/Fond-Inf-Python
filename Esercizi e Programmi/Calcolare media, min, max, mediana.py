# Chiedere all'utente tre numeri a, b, c
# Calcolare il minimo
# Calvolare il massimo
# Calcolare la media
# Calcolare la mediana

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

minimo = min(a, b, c)
massimo = max(a, b, c)

media = (a+b+c)/3

mediana = a + b + c - minimo - massimo

print("Il minimo vale: ", minimo)
print("Il massimo vale: ", massimo)
print("La media vale: ", media)
print("La mediana vale: ", mediana)