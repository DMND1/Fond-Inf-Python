# Scrivete un programma che acquisisca dall'utente la descrizione di una carta da gioco, usando la seguente notazione abbreviata:
# A     Ace
# 2..10 Valore della carta
# J     Jack
# Q     Queen
# K     King

# D     Diamonds
# H     Hearts
# S     Spades
# C     Clubs

# Il programma deve, poi, visualizzare la descizione completa della carta. Ad esempio:
# Enter the card notation: QS
# Queen of spades

carta_short = input("Immettere la carta in notazione abbreviata: ")

simbolo = carta_short[len(carta_short)-1]

if simbolo == "D":
    simbolo = "Diamonds"
elif simbolo == "H":
    simbolo = "Hearts"
elif simbolo == "S":
    simbolo = "Spades"
elif simbolo == "C":
    simbolo = "Clubs"
    
valore = carta_short[0]

if len(carta_short) == 3:
    risultato = "Ten of " + simbolo
else:                                       # ossia: elif len(carta_short) == 2 in questo caso particolare, poiché l'input è sempre o 2 o 3
    if valore == "A":
        risultato = "Ace of " + simbolo
    elif valore == "J":
        risultato = "Jack of " + simbolo
    elif valore == "Q":
        risultato = "Queen of " + simbolo
    elif valore == "K":
        risultato = "king of " + simbolo
    elif valore == "1":
        risultato = "One of " + simbolo
    elif valore == "2":
        risultato = "Two of " + simbolo
    elif valore == "3":
        risultato = "Three of " + simbolo
    elif valore == "4":
        risultato = "Four of " + simbolo
    elif valore == "5":
        risultato = "Five of " + simbolo
    elif valore == "6":
        risultato = "Six of " + simbolo
    elif valore == "7":
        risultato = "Seven of " + simbolo
    elif valore == "8":
        risultato = "Eight of " + simbolo
    elif valore == "9":
        risultato = "Nine of " + simbolo

print(risultato)