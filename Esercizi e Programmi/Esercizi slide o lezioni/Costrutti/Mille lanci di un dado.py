# Scrivere un programma che simuli mille lanci di un dado e che al termine stampi, per ogni faccia del dado, quante volte è uscita

# pseudocodice:
# import random
# numero1 = 0
# numero2 = 0
# numero3 = 0
# numero4 = 0
# numero5 = 0
# numero6 = 0
# ripetere mille volte un lancio di dado: (from i in range(1,1001))
# se la faccia è 1 addiziona 1 a numero1
# altrimenti se la faccia è 2 addiziona 1 a numero2
# ...
# altrimenti addiziona 1 a numero 6

# ciclo:
# for i in range(1,1001) :
#   faccia = random.randint(1,6)
#       if faccia == 1 :
#           numero1 = numero1 + 1
#       elif faccia == 2 :
#           numero2 = numero2 + 1
#       elif faccia == 3 :
#           numero3 = numero3 + 1
#       elif faccia == 4 :
#           numero4 = numero4 + 1
#       elif faccia == 5 :
#           numero5 = numero5 + 1
#       else:
#           numero6 = numero6 + 1

# stampa il risultato

import random

numero1 = 0
numero2 = 0
numero3 = 0
numero4 = 0
numero5 = 0
numero6 = 0

for i in range(0,1000) :            # Che equivale a: for i in range(1000)
    faccia = random.randint(1,6)
    if faccia == 1 :
        numero1 +=  1
    elif faccia == 2 :
        numero2 +=  1
    elif faccia == 3 :
        numero3 +=  1
    elif faccia == 4 :
        numero4 +=  1
    elif faccia == 5 :
        numero5 +=  1
    else:
        numero6 += 1

print("Il numero 1 è uscito:",numero1,"volte")
print("Il numero 2 è uscito:",numero2,"volte")
print("Il numero 3 è uscito:",numero3,"volte")
print("Il numero 4 è uscito:",numero4,"volte")
print("Il numero 5 è uscito:",numero5,"volte")
print("Il numero 6 è uscito:",numero6,"volte")