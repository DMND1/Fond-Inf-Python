# date due stringhe vedere se una è un anagramma dell'altra, tutti i caratteri delle stringhe sono diversi
# Esempio: rosa, raso, orsa sono anagrammi

# se le due stringhe hanno la stessa lunghezza
# se la prima lettera della stringa 1 è contenuta nella seconda e
# se la sedonda lettera della stringa 1 è contenuna nella seconda e
# ...
# se tutte le lettere della stringa 1 sono contenuto nella secondo: allora la parola è palindroma

stringa1 = input("Inserire la stringa 1: ")
stringa2 = input("Inserire la stringa 2: ")

Anagramma = False

if len(stringa1)==len(stringa2):
    if all (c in stringa1 for c in stringa2):
        Anagramma = True

if Anagramma == False:
    risposta = "Le due stringhe non sono anagrammi"
else:
    risposta = "Le due stringhe sono anagrammi"

print(risposta)