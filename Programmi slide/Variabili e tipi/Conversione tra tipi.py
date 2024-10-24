targa = "DE" + 295 + "WK" # Errore: 295 non è una stringa

str(123) # converte til valore in stringa

targa = "DE" + str(123) + "WK"

print(targa)


# si può anche fare con le variabili
a = 321

targa = "DE" + str(a) + "WK"

print(targa)


print(int("12.4")) # Da errore perché la stringa "12.4" non è un intero
print(int(float("12.4"))) # stampa 12