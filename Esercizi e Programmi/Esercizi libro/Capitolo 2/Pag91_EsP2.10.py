# Scrivere un programma che aiuti l'utente a decidere se convenga acquistare un'automobile con motore ibrido. I dati acquisiti dal programma sono:

# - Il costo di una nuova automobile
# - Una stima delle miglia percorse in un anno
# - Una stima del costo del carburante
# - L'efficienza del motore in miglia percorse per gallone
# - Una stima del prezzo di vendita dell'automobile usata dopo 5 anni

# Calcolare il costo totale relativo al possesso e alla gestione dell'auto per 5 anni. Trovare sul Web prezzi realistici per un'auto ibrida nuova e usata,
# oltre a quelli di un'auto simile con motore a benzina. Esegui il programma due volte, usando il prezzo attuale del carburante e una percorrenza annuale di 15000 miglia

costo_auto = float(input("Costo dell'automobile nuova: "))
miglia_1_anno = float(input("Miglia percorse in un anno: "))
costo_carburante = float(input("Costo carburante per un gallone: "))
eff_motore = float(input("Efficienza del motore in miglia percorse per gallone: "))
stima_prezzo_5_anni = float(input("Stima del prezzo di vendita automobile usata dopo 5 anni: "))

costo_tot_5_anni = costo_auto + (miglia_1_anno / eff_motore) * costo_carburante * 5
costo_tot_5_anni_vendita = costo_tot_5_anni - stima_prezzo_5_anni

print("Il costo totale relativo al possesso e alla gestione dell'auto per 5 anni ammonta a:", costo_tot_5_anni)
print("Se inoltre si decide di vendere l'automobile esso sarà:", costo_tot_5_anni_vendita)


"""
Dati usati per la prova (presi da ChatGPT):

- Miglia percorse all'anno: 15000
- Costo del carburante per gallone: $3.5

1. Automobile ibrida
- Costo iniziale: $28000
- Efficienza carburante: 50 miglia per gallone
- Prezzo stimato di rivendita dopo 5 anni: $14000

2. Automobile a benzina
- Costo iniziale: $23000
- Efficienza carburante: 30 miglia per gallone
- Prezzo stimato di rivendita dopo 5 anni: $10000

Con tali dati si avrà: 

1. Automobile ibrida
Il costo totale relativo al possesso e alla gestione dell'auto per 5 anni ammonta a: 33250.0
Se inoltre si decide di vendere l'automobile esso sarà: 19250.0

2. Automobile a benzina
Il costo totale relativo al possesso e alla gestione dell'auto per 5 anni ammonta a: 31750.0
Se inoltre si decide di vendere l'automobile esso sarà: 21750.0

"""