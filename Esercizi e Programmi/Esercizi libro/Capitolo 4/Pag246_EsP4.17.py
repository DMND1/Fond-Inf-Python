# Numeri primi. Scrivete un programma che chieda all'utente un numero intero e, poi, visualizzi tutti i numeri primi minori o uguali a tale numero. Se, ad esempio, 
# l'utente fornisce il numero 20, il programma deve visualizzare:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19

# leggi n
# n_primo = False
# mentre n_primo == False:
# se n ha un divisore (intero) diverso da 1 e n:
#   n non è primo : n_primo = False
#   n = n - 1
# altrimenti (cioè n è primo):
#   stampa n
#   n = n - 1
# se n-1 ha un divisore (intero) diverso da 1 e n:
#   n non è primo : n_primo = False
#   n = n - 1
# altrimenti (cioè n è primo):
#   stampa n
#   n = n - 1
# (ripetetere tale operazione fino a che n = 2)
# altrimenti se n ha come unico divisore se stesso:
#   n è primo : n_primo = True
#   stampa n

n = int(input("Inserire un numero intero: "))

# Inizializzazione variabili
non_primo = False
i = 2   # Con "i" intendo i divisori

# Inizio ciclo
while n >= 2:
    # Mentre n_primo è falso
    while non_primo == False:
        # Se n è divisibile per i e se n è diverso da i
        if n % i == 0 and n != i:
            # Ossia abbiamo trovato un divisore di n diverso da 1 e da n stesso
            non_primo = True
        # Altrimenti se n è l'unico divisore di se stesso (oltre all'1), ossia se n è primo
        elif n == i:
            # Stampalo
            print(n)
            # Concludi il ciclo, abbiamo trovato un numero primo
            break
        # Altrimenti
        else:
            # Aumenta di 1 la variabile i, ossia prova a vedere se il prossimo numero intero è un divisore di n
            i += 1
    # Reset delle varabili
    i = 2
    non_primo = False
    # Diminuisco n di 1
    n = n - 1

# In teoria tale programma stampa i numeri primi in ordine contrario rispetto all'esempio del libro, anche se nella consegna non viene specificato l'ordine.
# Per questo il programma diventerebbe:

n = int(input("Inserire un numero intero: "))

# Inizializzazione variabili
non_primo = False
i = 2   # Con "i" intendo i divisori
cont = 2

# Inizio ciclo
while cont <= n:
    # Mentre n_primo è falso
    while non_primo == False:
        # Se n è divisibile per i e se n è diverso da i
        if cont % i == 0 and cont != i:
            # Ossia abbiamo trovato un divisore di n diverso da 1 e da n stesso
            non_primo = True
        # Altrimenti se n è l'unico divisore di se stesso (oltre all'1)
        elif cont == i:
            # Ossia se n è primo, stampalo
            print(cont)
            # Concludi il ciclo, abbiamo trovato un numero primo
            break
        # Altrimenti
        else:
            # Aumenta di 1 la variabile i, ossia prova a vedere se il prossimo numero intero è un divisore di n
            i += 1
    # Reset delle varabili
    i = 2
    non_primo = False
    # Aumento di 1 il contatore
    cont = cont + 1