# - Dizionario che per ogni parola mette tutti gli anagrammi
#       come chiave deve aver le lettere in ordine alfabetico, per esempio con roma: "amor"


### Funzioni ###
"""
# Trovare gli anagrammi di una parola       # Tempo di calcolo: 0.7892267999995966 per 1000_parole_italiane_comuni.txt
def trovaAnagrammi(parola, nome_file):
    parola = parola.strip("\n")
    lista_anagrammi = []

    file = open(nome_file, "r", encoding="utf-8")


    for parola_file in file:
        parola_file = parola_file.strip("\n")
        if len(parola) == len(parola_file):
            anagramma = True
            for lettera in parola_file:
                if parola_file.count(lettera) != parola.count(lettera):
                    anagramma = False
            # Mettere gli anagrammi di tale parola in una lista
            if anagramma:
                lista_anagrammi.append(parola_file)

    file.close()

    return lista_anagrammi
"""
# Trovare gli anagrammi di una parola       # Tempo di calcolo: 0.49013899999954447 per 1000_parole_italiane_comuni.txt
def trovaAnagrammi(parola, nome_file):
    parola = parola.strip("\n")
    lista_anagrammi = []

    file = open(nome_file, "r", encoding="utf-8")

    parola_lista = list(parola)
    parola_lista.sort()

    for parola_file in file:
        parola_file = parola_file.strip("\n")
        if len(parola) == len(parola_file):
            parola_file_lista = list(parola_file)
            parola_file_lista.sort()
            if parola_file_lista == parola_lista:
                lista_anagrammi.append(parola_file)

    file.close()

    return lista_anagrammi

# Modifica del dizionario che ha come chiave le lettere in ordine alfabetico della parola e come valore la lista creata
def dizionarioAnagrammi(parola, dizionario, lista_anagrammi):
    chiave = ""

    parola_lista = list(parola)
    parola_lista.sort()

    for lettera in parola_lista:
        chiave += lettera

    dizionario[chiave] = lista_anagrammi



### Programma ###
from time import perf_counter

nome_file = "C:\Fond-Inf-Python\Risorse\\1000_parole_italiane_comuni.txt"
file = open(nome_file, "r", encoding="utf-8")
dizionario = {}

t1_start = perf_counter()

for parola in file:
    parola = parola.strip("\n")
    lista_anagrammi = trovaAnagrammi(parola, nome_file)
    if lista_anagrammi != [parola]:
        dizionarioAnagrammi(parola, dizionario, lista_anagrammi)

t1_stop = perf_counter()

file.close()

print(dizionario)
print("Tempo di calcolo:", t1_stop - t1_start)