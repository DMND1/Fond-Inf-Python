# Somma
def piu(x,y):
    if y == 1:
        return x + 1
    else:
        return piu(x, y-1) + 1

print(piu(5, 7))

# Prodotto
def per(x,y):
    if y == 1:
        return x
    else:
        return per(x, y-1) + x
    #   return piu(per(x, y-1), x)

print(per(5,7))