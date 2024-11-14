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

# Soluzione alternativa: controllare se i caratteri i cui indici hanno somma len(frase) sono uguali
# Per esempio: anna: "a" = "a" , "n"= "n"
# leggi s
# i = 0
# TrovatoDiverso = False
# mentre i è minore di len(frase)//2
#   se s[i] != s[len(frase)-1-i]
#       TrovatoDiverso = True
#   i = i +1
# if not TrovatoDiverso == True:
#   stampa vero (è palindromo)
# else:
#   stampa falso

s = input("Stringa: ")

trovato_diverso = False
i = 0

while (i < len(s)//2) and not trovato_diverso:
    j = len(frase)-1-i
    if s[i] != s[j]:
        trovato_diverso = True
    i = i + 1

# O in alternativa: 
while (i < len(s)//2):
    j = len(frase)-1-i
    if s[i] != s[j]:
        trovato_diverso = True
        break                   # Per terminare il ciclo se si trova un carattere diverso dal corrispondente
    i = i + 1

if not trovato_diverso == True:
    print("Vero")
else:
    print("Falso")