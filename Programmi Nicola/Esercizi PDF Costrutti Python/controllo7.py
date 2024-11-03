#verificare che un numero dato contenga la cifra 7

num = str(input("inserisci un numero intero da controllare: "))
true = 0
i = 0
while i<len(num):
    if num[i] == "7":
        true = 1
    i = i + 1

if true !=0:
    print("il numero ha la cifra 7")
else:
    print("il numero non contiene la cifra 7")


