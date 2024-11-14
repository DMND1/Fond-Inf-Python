a = str(input("Inserisci stringa: "))
i = 0
c = 0
for i in range(len(a)):
    if a[i] == a[len(a)-1-i]:
        c = c + 1
if c == len(a):
    print("La stringa è palindroma")
else:
    print("La stringa non è palindroma")

