# Scrivete un programma che legga una stringa e visualizzi i messaggi appropriati, dopo aver verificato se:
# - contiene soltanto lettere
# - contiene soltanto lettere maiuscole
# - contiene soltanto lettere minuscole
# - contiene soltanto cifre
# - contiene soltanto lettere e cifre
# - inizia con una lettera maiuscola
# - termina con un punto


stringa_originale = input("Inserire una stringa: ")
stringa = stringa_originale.replace(".","")

# Inizializzazione variabili
prima_lettera = stringa[0]

# La stringa contiene soltanto lettere
if stringa.isalpha():
    risultato = "La stringa contiene solo lettere"

    # La stringa contiene soltanto lettere maiuscole
    if stringa.isupper():
        risultato = risultato + " maiuscole"

    # La stringa contiene soltanto lettere minuscole
    elif stringa.islower():
        risultato = risultato + " minuscole"

# La stringa contiene soltanto cifre
elif stringa.isdigit():
    risultato = "La stringa contiene solo cifre"

# La stringa contiene soltanto lettere e cifre
elif stringa.isalnum():
    risultato = "La stringa contiene soltato lettere e cifre"


# La stringa Inizia con una lettera maiuscola
if prima_lettera.isupper() and not stringa_originale.endswith("."):
    risultato = risultato + " e la prima lettera è maiuscola"
elif prima_lettera.isupper() and stringa_originale.endswith("."):
    risultato = risultato + ", la prima lettera è maiuscola"

# La stringa termina con un punto
if stringa_originale.endswith("."):
    risultato = risultato + " e termina con un punto"

print(risultato)