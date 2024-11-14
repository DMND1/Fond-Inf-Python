# Scrivete un programma che legga una parola e visualizzi il numero di vocali presenti in essa (per questo esercizio assumete che le vocali siano a e i o u y). Se ad esempio l'utente
# fornisce la stringa "Harry", il programma deve visualizzare il messagio: 2 vowels

parola = input("Inserire una parola: ")

vocali = "aeiouy"
num_vocali = 0

for i in range(len(parola)):
    if parola[i] in vocali:
        num_vocali += 1

print("Il numero di vocali è:", num_vocali)