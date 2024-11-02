# Realizzare un programma che scriva le cifre binarie di un intero dato in ingresso

# Peusocodice: 
# leggi n

# n % 2             ultima cifra
# n // 2 % 2        penultima cifra
# n // 2 // 2 % 2   terzultima cifra
# ...               ...

# Il programma deve continuare fino a quando la divisione intera non ridà 0
# Implementare un ciclo che continua fino a quando questa condizione è soddisfatta

# while n // 2 != 0 :
#   risultato = str(n // 2 % 2) + risultato
#   n = n // 2

n = int(input("Numero intero da convertire in binario: "))

risultato = str(n % 2)     # Ultima cifra

while n // 2 != 0 :
    risultato = str(n // 2 % 2) + risultato
    n = n // 2

# Si osservi che se n = 0 allora il risultato vale 0 e il ciclo non parte

print("Il numero in base 2 è:",risultato)