# Scrivete un programa che legga una parola e visualizzi ciascuno dei suoi caratteri su una riga, da solo, ordinatamente

stringa = input("Inserire una parola: ")

for i in range(0,len(stringa)):
    print(stringa[i])