# Scrivete una funzione, scramble(word), che restitiusca una versione "mescolata" di una data parola, scambiando a caso due caratteri tra loro, evitando che il primo e l'ultimo
# carattere della parola siano coinvolti nello scambio. Poi, scrivete un programma che legga parole e le visualizzi dopo averle sottoposte a "mescolamento" tramite tale funzione.

def scramble(word):
    from random import randint

    if len(word) <= 3:
        return word
    else:
        while True:
            pos_car1 = randint(1,len(word)-2)
            pos_car2 = randint(1,len(word)-2)
            if pos_car1 < pos_car2:
                break

        word = word[:pos_car1] + word[pos_car2] + word[pos_car1+1:pos_car2] + word[pos_car1] + word[pos_car2+1:]

        return word

print(scramble("Ciao")) # Stampa Caio (l'unica possibile soluzione)


# Programma
parola = input("Inserire una parola: ")

risposta = ""

while parola != "0":
    risposta += scramble(parola) + " "
    parola = input("Inserire una parola(scrivere 0 per terminare): ")

print(risposta)