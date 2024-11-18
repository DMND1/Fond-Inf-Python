# Scrivete un programma un programma che chieda all'utente una singola lettera dell'alfabeto, visualizzando poi il messaggio "Vocale" o "Consonante". Se l'utente non digita una lettera
# oppure digita una stringa di lunghezza maggiore di uno, visualizzate un messaggio d'errore

lettera = input("Inserire una singola lettera: ")

vocali = "aeiouy"

if len(lettera) > 1 or lettera == "":
    risposta = "Input non valido"
elif lettera.isdigit():
    risposta = "Input non valido"
elif lettera.isalpha():
    if lettera in vocali:
        risposta = "Vocale"
    else:
        risposta = "Consonante"
else:
    risposta = "Input non valido"

print(risposta)