def contiene7(n):
    n_str = str(n)
    return "7" in n_str

l = []

for i in range(1000):
    if contiene7(i):
        l.append(i)

for el in l:
    print(el)