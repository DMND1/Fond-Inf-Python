# Scrivete un programma che legga tre stringhe e le visualizzi in ordine lessicografico. Ad esempio:
# Enter a string: Charlie
# Enter a string: Able
# Enter a string: Baker
# Able
# Baker
# Charlie

parola1 = input("Prima parola: ")
parola2 = input("Seconda parola: ")
parola3 = input("Terza parola: ")

risultato = "Le parole in ordine sono: "

if parola1 <= parola2 <= parola3:
    risultato += parola1 + " " + parola2 + " " + parola3
elif parola1 <= parola3 <= parola2:
    risultato += parola1 + " " + parola3 + " " + parola2
elif parola2 <= parola1 <= parola3:
    risultato += parola2 + " " + parola1 + " " + parola3
elif parola2 <= parola3 <= parola1:
    risultato += parola2 + " " + parola3 + " " + parola1
elif parola3 <= parola1 <= parola2:
    risultato += parola3 + " " + parola1 + " " + parola2
elif parola3 <= parola2 <= parola1:
    risultato += parola3 + " " + parola2 + " " + parola1

print(risultato)