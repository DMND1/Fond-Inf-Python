# trovare la stringa più lunga in ls
ls = ["gli", "i", "il", "la", "le", "lo","Napoli"]

s_lunga = len(ls[0])
s_corta = len(ls[0])
stringa_min = ls[0]
stringa_max = ls[0]

for i in ls:
    if len(i) < s_corta:
        s_corta = len(i)
        stringa_min = i
    elif len(i) > s_lunga:
        s_lunga = len(i)
        stringa_max = i

print("La stringa più corta è:", stringa_min)
print("La stringa pià lunga è:", stringa_max)