values = []                     # con n elementi
target = 5

def liinearSearch(values, target):
    for i in range(len(values)):    # i da 0 fino a n-1: in totle (3n + 1)x:
        if values[i] == target:         # 2 operazioni
            return i                    # 1 operazione
    return -1                       # 1 operazione (eventualmente)

# nel caso peggiore si ha:
# T(n) = O(n)
# T(n) = Ω(n)
# T(n) = Θ(n)