def elimina(l, e):
    i = 0
    c = []
    while i < len(l):
        if l[i] != e:
            c.append(l[i])
            i += 1
        else:
            i += 1
    return c
l = []
a = 1
while a != 0:
    a = int(input("Inserisci elemento nella lista: "))
    l.append(a)
e = int(input("Inserisci numero indesiderato: "))
c = elimina(l, e)
print(c[:len(c)-1])
