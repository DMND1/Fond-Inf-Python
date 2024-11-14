# Scrivete un programma che legga una parola e visualizzi tutte le sue sottostringhe, ordinate per lunghezza crescente. Se, ad esempio, l'utente fornisce 
# la stringa "rum", il programma deve visualizzare:

# r (1)
# u (2)
# m (3)

# ru (1,2)
# rm (1,3)
# um (2,3)

# rum (1,2,3)

# Oss: numero_di_casi = 2 ** len(parola) - 1

# Esempio: caso
#   (i)
# c (1)
# a (2)
# s (3)
# o (4)

#    (x,y)
# ca (1,2)
# cs (1,3)
# co (1,4)

#    (x+1,y)
# as (2,3)
# ao (2,4)

#    (x+2,y)
# so (3,4)

#     (x,y,z)
# cas (1,2,3)
# cao (1,2,4)

# cso (1,3,4)

# aso (2,3,4)


# caso (1,2,3,4)