# - Estrai i verbi, tutti le parole che finiscono per are, ere e ire

nome_file = "C:\Fond-Inf-Python\Risorse\\1000_parole_italiane_comuni.txt"
file = open(nome_file, "r", encoding="utf-8")

nome_file_modificato = "C:\Fond-Inf-Python\Esercizi e Programmi\Esercizi slide o lezioni\Tipi strutturati\File\\verbi.txt"
file_da_scrivere = open(nome_file_modificato, "w", encoding="utf-8")


for parola in file:
    # ciaociao
    parola = parola.strip("\n")
    if len(parola) >= 3 and parola[len(parola) - 3:] == "are" or parola[len(parola) - 3:] == "ere" or parola[len(parola) - 3:] == "ire":
        file_da_scrivere.write(parola + "\n")

file.close()
file_da_scrivere.close()