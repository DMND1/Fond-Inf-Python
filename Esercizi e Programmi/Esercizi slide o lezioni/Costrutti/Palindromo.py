# L'utente inserisce una stringa, verificare se la stringa è palindroma o meno e stampare il risultato

frase_originale = input("Parola o frase: ")

frase = frase_originale.lower()
frase = frase.replace(" ", "")

frase_palindroma = ""
lunghezza_frase = (len(frase) + 1)

for i in range(1, lunghezza_frase):
    frase_palindroma = frase_palindroma + frase[-i]

# In alternativa si può anche scrivere:
# for i in range(-1, -lunghezza_frase, -1):
#     frase_palindroma = frase_palindroma + frase[i]

if frase == frase_palindroma and " " in frase_originale:
    risposta = "Le frase è palindroma"
elif frase == frase_palindroma and not(" " in frase_originale):
    risposta = "Le parola è palindroma"
elif frase != frase_palindroma and " " in frase_originale: 
    risposta = "Le frase non è palindroma"
elif frase != frase_palindroma and not(" " in frase_originale): 
    risposta = "Le parola non è palindroma"

print(risposta)