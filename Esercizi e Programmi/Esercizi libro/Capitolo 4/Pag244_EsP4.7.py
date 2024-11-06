# Traducete in un programma Python la seguente descrizione in pseudocodice (vedi libro), che permuta in modo casuale i caratteri di una stringa:

import random

word = input("Digitare una parola: ")
# Ciao

for c in range(0,len(word)):
    i = random.randint(0,len(word)-2)
    j = random.randint(i+1,len(word)-1)
    first = word[0:i]
    middle = word[i+1:j]
    last = word[j+1:len(word)]
    final_word = first + word[j] + middle + word[i] + last

print(final_word)