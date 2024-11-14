# creiamo la lista l1 con gli input dell'utente
numero_stringa = input("Inserire un numero (scrivere stop per fermarsi): ")
li = []

while numero_stringa != "stop":
    numero = int(numero_stringa)
    li.append(numero)
    numero_stringa = input("Inserire un numero (scrivere stop per fermarsi): ")

print("La lista di numeri è:", li)


# trovare il massimo elemento in li (senza usare la funzione max)
minimo = li[0]
massimo = li[0]

for i in li:
    if i < minimo:
        minimo = i
    elif i > massimo:
        massimo = i

print("Il massimo vale:", massimo)
print("Il minimo vale:", minimo)


"""
# altrimenti sempre per trovare il massimo elemento in li (senza usare la funzione max)
li.sort()

print("Il massimo vale:", li[len(li)-1])
print("Il minimo vale:", li[0])
"""

# trovare la stringa più lunga in ls
ls = ["gli", "i", "il", "la", "le", "lo"]

s_lunga = len(ls[0])
s_corta = len(ls[0])
stringa_min = ls[0]
stringa_max = ls[0]

for i in ls:
    if len(i) < s_corta:
        s_corta = len(i)
        stringa_min = i
    elif len(i) > s_lunga:
        s_lunga = len(i)
        stringa_max = i

print("La stringa più corta è:", stringa_min)
print("La stringa pià lunga è:", stringa_max)


# stampare tutti gli elementi pari di li
li = [1,2,3,4,56,5,4,3,2,1]

for i in range(0,len(li),2):
    print(li[i])


# Raccogliere in una lista tutti gli elementi di li minori di 10
li = [1,2,3,4,56,5,4,3,2,1,88,11]
lista = []

for i in li:
    if i < 10:
        lista.append(i)

print("La lista che contiene tutti gli elementi di li minori di 10 è:", lista)


# fornire una lista con le lunghezze delle stringhe in ls
ls = ["gli", "i", "il", "la", "le", "lo"]
lista_lunghezze = []

for i in ls:
    lista_lunghezze.append(len(i))

print(lista_lunghezze)