#simulare mille lanci di un dado e scrivere alla fine quante volte le faccie sono uscite
import random
i = 0
r = 0
r1,r2,r3,r4,r5,r6= 0,0,0,0,0,0

while i < 1000:
    r = random.randint(1 , 6)
    if r == 1:
        r1 = r1 + 1
    elif r == 2:
        r2 = r2 +1
    elif r == 3:
        r3 = r3 + 1
    elif r == 4:
        r4 = r4 +1
    elif r == 5:
        r5 = r5 +1
    elif r == 6:
        r6 = r6 + 1
    i = i + 1

print("Facce uscite: ",r1, " ",r2, " ", r3 , " ", r4, " ", r5, " ", r6)