#Scriviamo un programma che, inserita una stringa, stampi la stringa col primo carattere in maiuscolo

print("inserisci il nome")

x = input()

x = x.lower()

nuovo_nome = x[0].upper() + x[1:len(x)]

print(nuovo_nome)
