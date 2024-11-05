# L'utente inserisce una stringa, verificare se la stringa è palindroma o meno e stampare il risultato

parola = input("Parola: ")
parola.lower()

parola_palindroma = ""
lunghezza_parola = - (len(parola) + 1)

for i in range(-1, lunghezza_parola, -1):
    parola_palindroma = parola_palindroma + parola[i]

if parola == parola_palindroma:
    risposta = "Le due parole sono palindrome"
else: 
    risposta = "Le due parole non sono palindrome"

print(risposta)