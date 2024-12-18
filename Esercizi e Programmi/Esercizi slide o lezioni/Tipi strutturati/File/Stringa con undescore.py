# - L'utente imette una stringa con degli underscore: c_s_
#       ritornare tutte le parole che potrebbero andare (hanno c come prima lettera e s come terza, e hanno len(stringa)=4)

# nome_file = "C:\Python\Fond-Inf-Python\Risorse\\1000_parole_italiane_comuni.txt"
nome_file = "C:\Fond-Inf-Python\Risorse\\1000_parole_italiane_comuni.txt"
file = open(nome_file, "r", encoding="utf-8")

tutto = file.read()
file.close()
lista_parole = tutto.split()

# parola_da_controllare = input("Inserire una parola: ")
parola_da_controllare = "c_s_"

lista_parole_possibili = []


for parola in lista_parole:
    controllo = False
    if len(parola) == len(parola_da_controllare):
        controllo = True
        for i in range(len(parola)):
            if parola_da_controllare[i] != "_" and parola_da_controllare[i] != parola[i]:
                controllo = False
    if controllo:
        lista_parole_possibili.append(parola)

print(lista_parole_possibili)