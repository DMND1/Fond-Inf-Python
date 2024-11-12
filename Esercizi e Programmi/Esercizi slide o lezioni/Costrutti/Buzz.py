# 6 giocatori si mettono in cerchio, un giocatore a caso inizia a contare da uno, si continuna in senso orario o anti orario, 
# ogni giocatore dice il numero successvio ma se un giocatore dice un numero multiplo di 7 o un numero che contiene 7 si deve dire pass, se

# scrivre un programma che stampi tutti i numeri esclusi i numeri multipli di 7 e i numeri che contengono il 7, 
# in tali casi deve stampare buzz (bass), fino a 100

# il numero contiene 7 senza stringhe:
# leggi n
# q = n
# r = q // 10
# se r == 7:
#   ...
# q = q // 10
# il numero è multiplo di 7:
# se n % 7 == 0:
#   il numero è multiplo

cifra_sette = False

for i in range(100):
    # Il numero contiene 7
    i = str(i)
    for c in range(0,len(i)):
            if i[c] == "7":
                cifra_sette = True
    # Ridefinisco i come intero
    i = int(i)
    # Controllo se il numero contiene 7 e se il numero è divisibile per 7
    if cifra_sette or i % 7 == 0:
        # Stampa
        print("Buzz")
    else:
        # Stampa
        print(i)
    # Ridefinisco cifra_sette come False
    cifra_sette = False

# Pseudo codice:
# per ogni numero (n) da 1 a 1000
# se n % 7 == 0:
#   print(buzz)
# altrimenti se n contiene 7:
#   print(buzz)
# altrimenti
#   print(n)

for n in range(1,1001):
    if n % 7 == 0:
        print("Buzz")
    else:
        contiene7 = False
        r = 0
        q = n
        while q != 0:
            r = q % 10
            if r == 7:
                contenie7 = True
            q = q // 10
        if contenie7 == True:
            print("Buzz")
        else:
            print(n)

# In alternativa
for n in range(1,1001):
    if (n % 7 == 0) or ("7" in str(n)):
        print("Buzz")
    else:
        print(n)