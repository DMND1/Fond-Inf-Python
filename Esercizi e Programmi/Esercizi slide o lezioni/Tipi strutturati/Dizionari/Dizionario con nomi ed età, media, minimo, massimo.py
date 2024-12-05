# Chiedere all’utente una lista di nomi di persone e poi, mostrando un nome la volta, chiedere l’età relativa alla persona con quel nome. Creare un 
# dizionario E con coppie nome/età

"""
# Creare la lista di nomi
lista_nomi = []

nome = input("Inserire un nome: ")

while nome == "stop":
    nome = input("Inserire un nome: ")

while nome != "stop":
    lista_nomi.append(nome)
    nome = input("Inserire un nome (scrivere stop per fermarsi): ")

print(lista_nomi)
"""

lista_nomi = ["Dario", "Luca", "Giovanni", "Eleonora"]
dizionario_nomi_età = {}

for nome in lista_nomi:
    dizionario_nomi_età[nome] = int(input("Inserire l'età di " + nome + ": ")) 

print(dizionario_nomi_età, end= "\n" * 2)



# Dato il dizionario E dell’esercizio precedente, trovare l’età media, la persona con l’età minima e quella con l’età massima.

dizionario_nomi_età = {'Dario': 11, 'Luca': 18, 'Giovanni': 49, 'Eleonora': 70}
print(dizionario_nomi_età)

# Età media
def mediaEtà(dizionario):
    lista_età = list(dizionario.values())
    numero_di_elem = len(dizionario)
    media = sum(lista_età) / numero_di_elem

    return media

print(mediaEtà(dizionario_nomi_età))    # Stampa 37.0

# In alternativa
def mediaEtà(dizionario):
    somma = 0
    for elem in dizionario:
        somma += dizionario[elem]

    return somma / len(dizionario)

print(mediaEtà(dizionario_nomi_età))    # Stampa 37.0



# La persona con l’età minima
def personaEtàMinima(dizionario):
    lista_età = list(dizionario.values())
    età_minima = min(lista_età)

    for elem in dizionario:
        if dizionario[elem] == età_minima:
            return elem

print(personaEtàMinima(dizionario_nomi_età))



# La persona con l’età massima
def personaEtàMassima(dizionario):
    lista_età = list(dizionario.values())
    età_massima = max(lista_età)

    for elem in dizionario:
        if dizionario[elem] == età_massima:
            return elem

print(personaEtàMassima(dizionario_nomi_età))