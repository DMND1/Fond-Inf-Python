# Scrivete un programma che legga una parola e visualizzi tutte le sue sottostringhe, ordinate per lunghezza crescente. Se, ad esempio, l'utente fornisce 
# la stringa "rum", il programma deve visualizzare:

# r (1)
# u (2)
# m (3)

# ru (1,2)
# um (2,3)

# rum (1,2,3)

# Esempio: caso
#   (i:c)   c = i + 1   ossia c = i + k dove k = 1
# c (0:1)
# a (1:2)
# s (2:3)
# o (3:4)

#    (i:c+1) c = i + 2  ossia c = i + k dove k = 2
# ca (0:2)
# as (1:3)
# so (2:4)

#    (i:c+2) c = i + 3  ossia c = i + k dove k = 3
# cas (0:3)
# aso (1:4)

#     (i:c+3)
# caso (0:4)

# leggi s
# Per tutti i k da 1 a len(s):
#   Per tutte le i da 0 a len(s)-k:
#       stampa s[i:i+k]
#   i = 0

s = input("Inserire una parola: ")

for k in range(1,len(s)+1):
    for i in range(0,len(s)-k+1):
        print(s[i:i+k])
    i = 0


print() # Metto uno spazio per non far attaccare le due esecuzioni
# Oppure:
for k in range(1,len(s)):
    for i in range(0,len(s)-k+1):
        print(s[i:i+k])
    i = 0
print(s)