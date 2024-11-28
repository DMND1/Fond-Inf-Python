n = int(input("Inserisci un numero naturale, digita 0 per terminare: ")) #inserisco il primo numero
ins = set() #Creo l'insieme dei numeri

insquad = set() #Creo gli insiemi dei quadrati e dei cubi
inscube = set()

while n != 0:
    ins.add(n)
    n = int(input("Inserisci un numero naturale, digita 0 per terminare: "))

# Continuo ad aggiungere numeri fino a quando non digito 0, poi inizializzo un ciclo for e inserisco tutti i quadrati e i cubi nei rispettivi insiemi per poi stamparli

for i in ins:
    quad = i**2
    cube = i**3
    insquad.add(quad)
    inscube.add(cube)

print(insquad)
print(inscube)