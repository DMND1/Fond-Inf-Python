# Fare il prodotto di tutti gli elementi in li
li = [1,2,3,4,5,8,11]   # prodotto = 10560

prodotto = 1
for i in li:
    prodotto *= i   # che equivale a: prodotto = prodotto * i

print(prodotto)