# Scrivete la funzoine: def countWords(string)
# che restituisca il numero di parole presenti nella stringa string. Le parole sono sequenze di caratteri separate da spazi. 
# Ad esempio, countWords("Mary had a little lamb") restitiusce 5

def countWords(string):
    if string == "":
        return 0
    else:
        AllSPace = True

        for carattere in string:
            if carattere != " ":
                AllSPace = False

        if AllSPace:
            return 0
        else:
            cont = 1
            for i in range(len(string)):
                if string[i] == " " and i != 0 and i != (len(string)-1) and string[i+1] != " ":
                    cont += 1
            return cont


print(countWords(" Mary had a little lamb "))   # Stampa 5
print(countWords("Mary "))                      # Stampa 1
print(countWords(""))                           # Stampa 0
print(countWords("    "))                       # Stampa 0