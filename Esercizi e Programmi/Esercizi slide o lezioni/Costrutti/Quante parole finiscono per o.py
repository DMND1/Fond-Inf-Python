# Supponete di avere una stringa, vogliamo sapere per quante parole finiscono per o, una parola è una sequenza di caratteri che termina per uno spazio

s = "Il caso del tempo meteo"
s = input("Inserire una frase o parola: ")
# risposta 3 in questo caso

cont = 0

#if s == "":
#    cont = 0

if len(s) == 1:
    if s == "o":
        cont +=1
elif len(s) >= 2:
    for i in range(1, len(s)):
        if s[i] == " " and s[i-1] == "o":
            cont += 1

    if s[len(s)-1] == "o":  # che equivale a if s[-1] == "o":
        cont += 1

print(cont)