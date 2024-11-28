def fattori(n): # restituisce la lista dei fattori di un numero
    lista_fattori = []

    if n == 1:
        lista_fattori.append(1)
    else:
        # Inizializzazione variabili
        i = 2
        # Inizio ciclo
        while i <= n:
            # Se i è un divisore (intero) di n
            if n % i == 0:
                # Stampa i
                lista_fattori.append(i)
                # Pongo n = al risultato di tale divisione intera
                n = n // i
                # Pongo i = 2, questo perché dobbiamo riniziare "da capo" a controllare tutti i divisori (interi) di n
                i = 2
            # Altrimenti se i non è un divisore di n
            else:
                # Incremento di 1 la variabile i, per provare il prossimo divisore intero
                i += 1

    return lista_fattori

print(fattori(70))