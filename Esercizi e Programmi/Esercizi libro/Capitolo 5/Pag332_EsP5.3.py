# Scrivete le seguenti funzioni:
# - def firstDigit(n)   # restituisce la prima cifra dell'argomento
# - def lastDigit(n)    # restituisce l'ultima cifra dell'argomento
# - def digits(n)       # restituisce il numero di cifre dell'argomento

# asssumo che n sia un intero qualsiasi

def firstDdigit(n):
    n = str(n)
    n = n.replace("-", "")
    return n[0]

def lastDigit(n):
    n = str(n)
    n = n.replace("-", "")
    return n[-1]

def digits(n):
    n = str(n)
    n = n.replace("-", "")
    return len(n)

n = int(input("Inserire un numero: "))

print(firstDdigit(n), lastDigit(n), digits(n))