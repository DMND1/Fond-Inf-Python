# - Rimario: prendere le parole e ordinarle per come finiscono, mettere insieme tutte le parole che finiscono allo stesso modo:
#       prendere tutte le parole, scriverle al contrario, ordinare in ordine alfabetico la lista, riscriverle al contrario



def invertiParole(lista, lista_output):
    for parola in lista:
        parola_inversa = ""
        for i in range(len(parola)-1, -1, -1):
            parola_inversa += parola[i]
        lista_output.append(parola_inversa)



# nome_file = "C:\Python\Fond-Inf-Python\Risorse\\1000_parole_italiane_comuni.txt"
nome_file = "C:\Fond-Inf-Python\Risorse\\1000_parole_italiane_comuni.txt"
file = open(nome_file, "r", encoding="utf-8")

tutto = file.read()
file.close()
lista_parole = tutto.split()

lista_rimario = []
invertiParole(lista_parole, lista_rimario)
lista_rimario.sort()

lista_finale = []
invertiParole(lista_rimario, lista_finale)

print(lista_finale)