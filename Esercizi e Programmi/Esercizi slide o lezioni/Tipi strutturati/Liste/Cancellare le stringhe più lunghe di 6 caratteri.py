# Cancellare tutte le stringhe più lunghe di 6 caratteri da ls
ls = ["gli", "i", "Agrigento", "il", "la", "le", "lo","Napoli Colera"]

for i in ls:
    if len(i) > 6:
        ls.remove(i)

print(ls)