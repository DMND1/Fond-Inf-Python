n = int(input("Inserisci un numero naturale, digita 0 per terminare: "))
ins = set()

insquad = set()
inscube = set()
while n != 0:
    ins.add(n)
    n = int(input("Inserisci un numero naturale, digita 0 per terminare: "))


for i in ins:
    quad = i**2
    cube = i**3
    insquad.add(quad)
    inscube.add(cube)

vuoto = set()
intersection = insquad.intersection(inscube) 

"""
Ho aggiunto un insieme intersezione fra l'insieme dei quadrati e quello dei cubi
e un insieme vuoto, in modo che controlli successivamente che i due insiemi siano disgiunti o meno'
"""

#Due insiemi sono disgiunti quando non hanno elementi comuni

if intersection == vuoto:
    print("disgiunti")
else:
    print("non disgiunti")
    