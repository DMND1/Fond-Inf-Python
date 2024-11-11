# Il gioco di Nim. ... vedere libro

from random import randint

numero_biglie = randint(10,100)


primo_giocatore_user = False
primo_giocatore_computer = False

primo_giocatore = randint(0,1)
if primo_giocatore == 0:
    print("Sarà il giocatore a muoversi per primo")
    primo_giocatore_user = True
else:
    print("Sarà il computer a muoversi per primo")
    primo_giocatore_computer = True


smart = False
dumb = False

smart_or_dumb = randint(0,1)
if smart_or_dumb == 0:
    smart = True
else:
    dumb = True

print("Il numero di biglie iniziali è:", numero_biglie)


if primo_giocatore_user == True:
    while numero_biglie != 0:
        x = int(input("Scegliere il numero di biglie da prelevare: "))
        if x > (numero_biglie / 2) and x != numero_biglie:
            print("Input non valido")
            break
        elif x == numero_biglie:
            print("Congratulazioni hai vinto contro il computer, prelevando l'ultima biglia")
        else:
            numero_biglie = numero_biglie - x
            print("Il numero di biglie ora è:", numero_biglie)
        if smart == True:
            print("---")
        elif dumb == True:
            x = randint(1,(numero_biglie // 2))
            print("Il computer ha scelto di togliere",x,"biglia/e")
            numero_biglie = numero_biglie - x
            print("Il numero di biglie ora è:", numero_biglie)

# ...