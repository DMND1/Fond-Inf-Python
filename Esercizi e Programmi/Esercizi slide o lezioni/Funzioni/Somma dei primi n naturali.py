# Realizzare una funzione ricorsiva che calcoli la somma dei primi n naturali.

def somma(n):
    if n == 1:
        return 1

    return n + somma(n-1)

print(somma(10))