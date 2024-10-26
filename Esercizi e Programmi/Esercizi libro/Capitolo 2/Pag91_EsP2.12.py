# Nomi diflle e loro estensioni. Scrivete un programma Che chieda all'utente di fornire Ia lettera corrispondente al disco su cui si trova un file (ad esempio, C),
# il percorso da seguire per trovarlo nel file system (ad esempio, \Windows\System), il nome del file (come Readme) e la sua estensione (txt). Poi, visualizzate il 
# nome completo del file, in questo esempio C: \Windows\System\Readme. txt (se usate un sistema Unix o Macintosh, ignorate la lettera iniziale e usate / invece di \ per 
# separare tra loro i norni delle cartelle).


disco = input("I disco su cui si trova il file: ")
percorso = input("Il percorso file per trovarlo nel file system: ")
nome = input("Il nome del file: ")
ext = input("L'estesione del file: ")

nome_completo = disco + ":" + percorso + "\\" + nome + "." + ext         # inoltre al posto di "\\" si può usare chr(92) che è \ in unicode

print("Il nome completo del file è:", nome_completo)

