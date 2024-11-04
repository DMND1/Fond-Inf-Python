# Scrivete un programma che legga un valore di temperatura seguito dalla lettera C per Celsius o F per Fahrenheit, poi visualizzi un messaggio che dica se, al livello 
# del mare e a quella temperatura, l'acqua si trova allo stato solido, liquido o gassoso

temp = input("Temperatura seguita da C per Celsius e F per Fahrenheit: ")
temp = temp.upper()                                 # In teoria non necessario se diamo per scontato che l'utente immetta C e F come maiuscole e non minuscole

unita_misura_temp = temp[len(temp)-1]               # Prendo l'ultima cifra della stringa
temperatura = float(temp.strip(" " + "C" + "F"))    # Tolgo dalla stringa tutto ciò che non è un numero

if unita_misura_temp == "C":
    if temperatura <= 0 and temperatura > -273.15:
        risultato = "stato solido"
    elif 0 < temperatura < 100:
        risultato = "stato liquido"
    elif temperatura <= -273.15:
        risultato = "damn water under absolute zero???"
    else:
        risultato = "stato gassoso"
elif unita_misura_temp == "F":
    if temperatura <= 32 and temperatura > -459.67:
        risultato = "stato solido"
    elif 32 < temperatura < 212:
        risultato = "stato liquido"
    elif temperatura <= -459.67:
        risultato = "damn water under absolute zero???"
    else:
        risultato = "stato gassoso"

print(risultato)