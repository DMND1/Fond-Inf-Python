def F(n):
    fattori = set()                 # 2 operazioni
    for i in range(2, n//2 + 1):    #   x(n/2) operazioni
        if n % i == 0:              #       2 operazioni
            fattori.add(i)          #       1 operazioni
    fattori.add(n)                  # 1

    return fattori                  # 1
                                    # In tutto: 3n/2 + 4

# T(n) = c(3n/2 + 4) = O(n)
# T(n) = Ω(n)
# T(n) = Θ(n)


if F(15).intersection(F(35)) != set():
    print("I numeri non sono coprimi")
else:
    print("I numeri sono coprimi")