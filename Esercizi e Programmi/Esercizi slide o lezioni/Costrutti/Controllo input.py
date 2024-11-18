# Chiedere all'utente un intero e controllare che effettivamente l'utente ha inserito un intero (stessa cosa per un float)

# Per i numeri interi
n = input("Inserire un intero: ")

if n.isdigit:
    if len(n) == 1:
        print("L'input è valido")
    elif len(n) > 1 and n[0] != "0":
        print("L'input è valido")
    else: 
        print("Input non valido")
else:
    print("Input non valido")

# Per i float
x = input("Inserire un numero in virgola mobile: ")
if x[0] != ".":
    contatore_punto = x.count(".")
    x = x.replace(".","")
    if x.isdigit and contatore_punto == 1:
        print("L'input è valido")
    else:
        print("Input non valido")
else:
    print("Input non valido")