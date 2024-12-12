# - Dizionario che per ogni parola mette tutti gli anagrammi
#       come chiave deve aver le lettere in ordine alfabetico, per esempio con roma: "amor"


### Funzioni ###
from time import perf_counter

def maxAnagrammi(dizionario):
    lista_max = []

    for lista_anagrammi in dizionario.values():
        if len(lista_anagrammi) > len(lista):
            lista_max = lista_anagrammi

    return lista_max



nome_file = "C:\Python\Fond-Inf-Python\Risorse\\60000_parole_italiane.txt"
# nome_file = "C:\Fond-Inf-Python\Risorse\\1000_parole_italiane_comuni.txt"
file = open(nome_file, "r", encoding="utf-8")


t1_start = perf_counter()

tutto = file.read()
file.close()
lista = tutto.split()
anagrammi = {}

for parola in lista:
    # calcolare la chiave
    chiave = ""
    caretteri = list(parola)
    caretteri.sort()
    for lettera in caretteri:
        chiave += lettera
    # inserire la parola in corrispondenza della chiave
    if chiave not in anagrammi:
        anagrammi[chiave] = [parola]
    else:
        anagrammi[chiave] = anagrammi[chiave] + [parola]
    
t1_stop = perf_counter()



print(anagrammi)
print(maxAnagrammi(anagrammi))
print("Tempo di calcolo:", t1_stop - t1_start)