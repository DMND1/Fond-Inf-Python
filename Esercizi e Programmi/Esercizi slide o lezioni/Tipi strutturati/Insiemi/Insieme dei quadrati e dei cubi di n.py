# Chiedendo all’utente un insieme di numeri naturali, creare l’insieme dei quadrati Q e quello dei cubi C dei numeri dati

n = input("Inserire un numero: ")

while n == "stop":
    n = input("Inserire un numero: ")

insieme = set()
quadrati = set()
cubi = set()

while n != "stop":
    n = int(n)
    insieme.add(n)
    n = input("Inserire un numero (scrivere stop per fermare il programma): ")

for i in insieme:
    quadrati.add(i ** 2)

for i in insieme:
    cubi.add(i ** 3)

print(insieme)
print(quadrati)
print(cubi)


# Dati gli insiemi Q e C dell’esercizio precedente, questi sono disgiunti? scrivere un programma per verificare la risposta.

if quadrati.intersectio(cubi) == {}:
    print("I due insiemi sono disgiunti")
else:
    print("I due insiemi hanno elementi in comune")