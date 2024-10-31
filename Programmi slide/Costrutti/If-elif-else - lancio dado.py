import random
faccia = random.randint(1, 6) #lancio del dado

if faccia == 1 :
    print("Uno")
elif faccia == 2 :
    print("Due")
elif faccia == 3 :
    print("Tre")
elif faccia == 4 :
    print("Quattro")
elif faccia == 5 :
    print("Cinque")
else:
    print("Sei")