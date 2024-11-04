# Aggiungete all'esercizio precedente la gestione degli errori: se l'utente fornisce un'unità di misura non valida per l'altitudine, visualizzate un messaggio d'errore 
# e terminate il programma

temp = input("Temperatura seguita da C per Celsius e F per Fahrenheit: ")
temp = temp.upper()                                         # In teoria non necessario se diamo per scontato che l'utente immetta C e F come maiuscole e non minuscole

unita_misura_temp = temp[len(temp)-1]                       # Prendo l'ultima cifra della stringa
temperatura = float(temp.strip(" " + "C" + "F"))            # Tolgo dalla stringa tutto ciò che non è un numero

alt = input("altitudine seguita da m per metri e f per piedi: ")
temp = temp.lower()                                         # In teoria non necessario se diamo per scontato che l'utente immetta m e f come minuscole e non maiuscole  

unita_misura_alt = alt[len(alt)-1]

if unita_misura_alt != "m" and unita_misura_alt != "f":
    print("Errore: immetere un'unità di misura corretta per l'altitudine")
else:
    altitudine = float(alt.strip(" " + "m" + "f"))
    
    if unita_misura_alt == "m":
        coeff_altitudine = altitudine / 300
    elif unita_misura_alt == "f":
        coeff_altitudine = altitudine / 1000

    punto_ebolizzione_C = 100 - 1 * coeff_altitudine
    punto_ebolizzione_F = (punto_ebolizzione_C * (9/5)) + 32    # Conversione da gradi Celsius a Fahrenheit

    if unita_misura_temp == "C":
        if temperatura <= 0 and temperatura > -273.15:
            risultato = "stato solido"
        elif 0 < temperatura < punto_ebolizzione_C:
            risultato = "stato liquido"
        elif temperatura <= -273.15:
            risultato = "damn water under absolute zero???"
        else:
            risultato = "stato gassoso"
    elif unita_misura_temp == "F":
        if temperatura <= 32 and temperatura > -459.67:
            risultato = "stato solido"
        elif 32 < temperatura < punto_ebolizzione_F:
            risultato = "stato liquido"
        elif temperatura <= -459.67:
            risultato = "damn water under absolute zero???"
    else:
        risultato = "stato gassoso"

    print(risultato)