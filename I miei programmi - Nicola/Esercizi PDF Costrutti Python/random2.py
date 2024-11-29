#simulare il lancio di due dadi mille volte e stampare il numero di lanci in cui i dadi hanno avuto la stessa faccia

import random

d1 = 0
d2 = 0
num = 0
for i in range (0,1000-1):
    d1 = random.randint(1 , 6)
    d2 = random.randint(1 , 6)
    if d1 == d2:
        num = num + 1


print("Numero di lanci effettuati con condizione: ",num)
