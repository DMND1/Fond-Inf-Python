# Chiedendo all’utente un insieme di numeri naturali, creare l’insieme dei quadrati Q e quello dei cubi C dei numeri dati

n = input("Inserire un numero: ")

while n == "stop":
    n = input("Inserire un numero: ")

quadrati = set()
cubi = set()

while n != "stop":
    n = int(n)
    quadrati.add(n ** 2)
    cubi.add(n ** 3)
    n = input("Inserire un numero (scrivere stop per fermare il programma): ")

print(quadrati)
print(cubi)


# Dati gli insiemi Q e C dell’esercizio precedente, questi sono disgiunti? scrivere un programma per verificare la risposta.

if quadrati.intersection(cubi) == set():
    print("I due insiemi sono disgiunti")
else:
    print("I due insiemi hanno elementi in comune")