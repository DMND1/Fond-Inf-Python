# Realizzare un programma che scriva le cifre binarie di un intero dato in ingresso

# Peusocodice: 
# leggi n

# n % 2             ultima cifra
# n // 2 % 2        penultima cifra
# n // 2 // 2 % 2   terzultima cifra
# ...               ...

# Il programma deve continuare fino a quando la divisione intera non ridà 0, ossia fin quando il quoziente non è zero
# Implementare un ciclo che continua fino a quando questa condizione è soddisfatta

# while n // 2 != 0 :
#   risultato = str(n // 2 % 2) + risultato
#   n = n // 2

n = int(input("Numero intero da convertire in binario: "))
base = int(input("Base del numero: "))

quoziente = n // base
resto = n % base

risultato = str(resto)     # Ultima cifra

while quoziente != 0 :
    resto_numero = quoziente % base
    risultato = str(resto_numero) + risultato
    quoziente = quoziente // base

# Si osservi che se n = 0 allora il quoziente e il risultato valgono 0 e il ciclo non parte

print("Il numero in base", str(base), "è:",risultato)

# Pseudocodice:
# leggi n
# mentre il quoziente non è zero (n diverso da 0): 
#   caclola q, r
#   n = q
#  