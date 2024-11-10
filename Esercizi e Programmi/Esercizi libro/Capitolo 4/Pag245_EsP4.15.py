# I numeri di fibonacci sono definiti da questa sequenza: (considerare il contenuto delle () come pedice)
# f(1) = 1
# f(2) = 1
# f(n) = f(n-1)+f(n-2)

# Che si può riformulare in questo modo:
# fold1 = 1
# fold2 = 1
# fnew = fold1 + fold2

# Fatto questo, eliminate fold2, che non serve più, e assegante fold1 a fold2, e fnew a fold1; quindi, ripetete quante volte volete.
# Realizzate un programma che chieda all'utente un numero intero e n e visualizzi l'n-esimo numero di Fibonacci, usando l'algoritmo appena visto


n = int(input("Numero intero n: "))

# I numeri 1 e 1 sono i primi due numeri della sequenza di fibonacci
fold1 = 1
fold2 = 1

# Se il numero inserito è diverso da 1 e da 2
if n != 1 and n != 2:
    # Inizio ciclo
    for i in range(n-2):
        fnew = fold1 + fold2
        fold2 = fold1
        fold1 = fnew
    # Stampo il risultato
    print("L'n-esimo numero di fibonacci è:", fnew)
# Se il numero inserito è 1 o 2
else:
    print("L'n-esimo numero di fibonacci è: 1")