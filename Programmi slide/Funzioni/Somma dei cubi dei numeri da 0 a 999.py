def cubo(x):
    ris = x ** 3
    return ris

def media(l):
    somma = sum(l)
    num_elementi = len(l)
    media = somma / num_elementi
    return media

l = []

for i in range(1000):
    l.append(cubo(i))

print(media(l))