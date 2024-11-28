a = {"Io", "Ganimede", "Callisto", "Europa"}

for satellite in a:
    print(satellite)    # L'ordine è deciso da Python
# Stampa:
# Ganimede
# Io
# Callisto
# Europa

b = {1,"uno", 2.0, "due"}   # Si possono inserire elementi di tipo eterogeneo

b = {1,"uno", 2.0, "due", (1,2,3,4,5)}  # All'interno di un insieme si possono mettere elementi che non mutano (unhashable)

# Per esempio se mettiamo una lista dentro un insieme da errore, poiché una lista è mutabile
b = {1,"uno", 2.0, "due", [1,2,3,4,5]}  # Da errore

# Al contrario è possibile mettere all'interno di una lista un insieme o un'altra lista
li = [1,"uno", {1,2,3}]

vuoto = {}  # Non è l'insieme vuoto ma un dizionario
print(type(vuoto)) # Stampa dict

vuoto = set()   # Questo è l'insieme vuoto
print(type(vuoto)) # Stampa set

c = set([2,3,4])
# ora ci vale:
c = {2,3,4}

c =  {"luna", "phobos"}

a.union(c)
# ritorna: {"Io", "Ganimede", "Callisto", "Europa", "luna", "phobos"}

print(a)    # stampa a originale, a rimane invariato

d = a.union(c)

a.issubset(d)
# ritorna True

a.intersection(c)
# ritorna set()

