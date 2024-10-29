# Lo pseudocodice seguente descrive come trasformare una stringa contenente un numero telefonico a dieci cifre (come "4155551212") in una stringa più facilmente leggibile.
# Con parentesi e trattini, secondo lo stile statunitense, come " (415) 555-1212".

# Prendere la stringa costituita dai primi tre caratteri e circondarla con parentesi tonde (questo é il prefisso, area code)
# Concatenare il prefisso con la stringa contenente i tre caratteri successivi, un trattino e la stringa costituita dagli ultimi quattro caratteri: si ottiene il numero 
# nel formato richiesto

# Traducete questo pseudocodice in un programrna Python che acquisisca un numero telefonico in ingresso, memorizzandolo in una stringa, per poi visualizzarlo 
# nel formato appena descritto.

numero = input("Numero di telefono: ")

area_code = "(" + numero[0:3] + ") "
stringa1 = numero[3:6] + "-"
stringa2 = numero[6:len(numero)]

print("Il numero di telefono secondo lo stile statunitense è: " + area_code + stringa1 + stringa2)