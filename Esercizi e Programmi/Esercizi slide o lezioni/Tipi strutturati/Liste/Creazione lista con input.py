# creiamo la lista l1 con gli input dell'utente
numero_stringa = input("Inserire un numero (scrivere stop per fermarsi): ")
li = []

while numero_stringa != "stop":
    numero = int(numero_stringa)
    li.append(numero)
    numero_stringa = input("Inserire un numero (scrivere stop per fermarsi): ")

print("La lista di numeri è:", li)