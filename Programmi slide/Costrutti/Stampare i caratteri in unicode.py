# stampa i caratteri di una stringa e il loro codice uni code

for c in "Salve!":      # c assume i valori ’S’,’a’,’l’,’v’,’e’,’!’
    print (c, ord(c))   # per ognuno stampa il suo codice unicodes


# Lo stesso programma con il ciclo while può essere scritto così: 

saluto = "Salve!"

i = 0
while i < len(saluto):
    print(saluto[i])
    i = i +1

# O in alternativa: 
while i != len(saluto):
    print(saluto[i])
    i = i + 1

# Quest'ultimo ciclo while è analogo al precedente perché quando i = len(saluto) il programma compie l'istruzione pass e si conclude