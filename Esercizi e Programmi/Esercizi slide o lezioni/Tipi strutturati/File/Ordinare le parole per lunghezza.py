# - Ordinare le parole per lunghezza

nome_file = "C:\Fond-Inf-Python\Risorse\\1000_parole_italiane_comuni.txt"

nome_file_modificato = "C:\Fond-Inf-Python\Esercizi e Programmi\Esercizi slide o lezioni\Tipi strutturati\File\\1000_parole_italiane_ordinate_per_lunghezza.txt"
file_da_scrivere = open(nome_file_modificato, "w", encoding="utf-8")

lungezza_parola_piu_lunga = len("precipitevolissimevolmente")

for i in range(1, lungezza_parola_piu_lunga + 1):
    file = open(nome_file, "r", encoding="utf-8")
    for parola in file:
        parola = parola.strip("\n")
        if len(parola) == i:
            file_da_scrivere.write(parola + "\n")
    file.close()

file_da_scrivere.close()

print("ciao")