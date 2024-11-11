# Scrivete un programma che legga un numero intero, n, e visualizzi, usando asterischi, un quadrato pieno e uno con il solo contorno, uno di fianco all'altro, 
# con il lato che misura n. Se, ad esempio, l'utente fornisce il numero 5, il programma deve visualizzare:

# ***** *****
# ***** *   *
# ***** *   *
# ***** *   *
# ***** *****

n = int(input("Inserire un numero intero: "))

# Inizializzazione variabili
cont = 1
riga_piena = "*" * n
riga_vuota = "*" + " " * (n-2) + "*"

# Inizio ciclo
while cont <= n:
    # Se il contatore è 1 o se il contatore è uguale al numero n preso in input
    if cont == 1 or cont == n:
        # Stampa 
        print(riga_piena + " " + riga_piena)
    else:
        print(riga_piena + " " + riga_vuota)
    # Aumento il contatore
    cont += 1