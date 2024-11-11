# Scrivete un programma che legga un numero intero, n, e visualizzi, usando asterischi, un rombo pieno il cui lato abbia lunghezza n. Se, ad esempio, l'utente fornisce il numero 4,
# il programma deve visualizzare:


# se n = 3

#    *
#   ***
#  *****
#   ***
#    *

# se n = 4
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# lunghezza_max = len(*******) = 1 + (n-1) * 2 = max. di c
# c = 1
# max. di n = n-1
#    *   = (lunghezza_max - n) * " " + ("*" * c)
#   ***  = (lunghezza_max - n - 1) * " " + ("*" * c + 2)
#  ***** = (lunghezza_max - n - 2) * " " + ("*" * c + 4)
# *******= (lunghezza_max - n - 3) * " " + ("*" * c + 6)

# n = 8 e  e c = 9
# lunghezza_max - n = 0

# n = n - 1 = 7
# c = c + 2 = 7

#  ***** =
#   ***  =
#    *   =

n = int(input("Inserire un numero intero: "))

ripetizioni = n + (n-1)
lunghezza_max = 1 + (n-1) * 2
c = 1
i = n

while i <= ripetizioni and c <= lunghezza_max:
    print((lunghezza_max - i) * " " + ("*" * c))
    i = i + 1
    c = c + 2

# ...