# Scrivete un programma che chieda all'utente una parola e visualizzi i primi tre caratteri, tre puntini e gli ultimi 3 caratteri

parola = str(input("La parola scelta (con almeno 6 caratteri) è: "))

parola = parola[0:3] + "..." + parola[len(parola)-3:len(parola)]

print(parola)