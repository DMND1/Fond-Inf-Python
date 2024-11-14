# Scrivete un programma che legga una parola e la visualizzi al contrario

stringa = input("Inserire una parola: ")

stringa_contrario = ""

for i in range(len(stringa)-1,-1, -1):
    stringa_contrario += stringa[i]

print(stringa_contrario)