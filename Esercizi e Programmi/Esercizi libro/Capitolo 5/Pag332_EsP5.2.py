# Scrivere le seguenti funzioni e progettate un programma che le collaudi
# - def allTheSame(x, y, z)     # restituisce True se gli argomenti sono tutti uguali
# - def allDifferent(x, y, z)   # restituisce True se tutti gli argomenti sono diversi
# - def sorted(x, y, z)         # restituisce True se gli argomenti sono in ordine crescente

# restituisce True se gli argomenti sono tutti uguali
def allTheSame(x, y, z):
    if x == y == z:
        return True
    else:
        return False
print(allTheSame(1,2,2))
print(allTheSame(1,2,3))
print(allTheSame(1,1,1), end="\n" + "\n")

# restituisce True se tutti gli argomenti sono diversi
def allDifferent(x, y, z):
    if x != y and y != z and z != x:
        return True
    else:
        return False
print(allDifferent(1,1,1))
print(allDifferent(1,2,2))
print(allDifferent(1,2,3), end="\n" + "\n")

# restituisce True se gli argomenti sono in ordine crescente
def sorted(x, y, z):
    if x <= y <= z:
        return True
    else: 
        return False

print(sorted(5,2,3))
print(sorted(1,2,3))