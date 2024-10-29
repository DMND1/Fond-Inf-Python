# Dare il resto. Realizzate un programma che aiuti un cassiere a dare il resto. II programma riceve due dati in ingresso: la somma da pagare e la quantità di 
# denaro ricevuta dal cassiere. Visualizzate il resto dovuto al cliente sotto forma di numeri di monete da un dollaro, da un quarto di dollaro (quarter), 
# da dieci centesimi (dime), da cinque centesimi (nickel) e da un centesimo (penny). Per evitare errori di arrotondamento, l'utente del programma deve fornire 
# entrambi i valori in centesimi, scrivendo, ad esempio, 274 invece di 2.74.

somma_da_pagare = int(input("Somma da pagare: "))
denaro_ricevuto = int(input("Denaro ricevuto dal cassiere: "))

# somma_da_pagare = 274
# denaro_ricevuto = 400

dollaro = 100
quarter = 25   # dollaro / 4
dime = 20      # dollaro / 10
nickel = 5     # dollaro / 20
penny = 1      # dollaro / 100

resto_tot = denaro_ricevuto - somma_da_pagare

# Per esempio: 
# resto_tot = 126
# resto da dare: 1 dollaro, 1 quarter, 1 penny

resto_dollari = resto_tot // dollaro                                                                                    # In questo caso resto_dollari = 26 // 100 = 1
resto_quarter = (resto_tot - resto_dollari * 100) // quarter                                                            # In questo caso resto_quarter = (126-100) // 25 = 1
resto_dime =  (resto_tot - resto_dollari * 100 -  resto_quarter * 25) // dime                                           # In questo caso resto_dime = (126-100-25) // 10 = 0
resto_nickel = (resto_tot - resto_dollari * 100 -  resto_quarter * 25 - resto_dime * 20) // nickel                      # ...
resto_penny = (resto_tot - resto_dollari * 100 -  resto_quarter * 25 - resto_dime * 20 - resto_nickel * 5) // penny     # In questo caso resto_penny = 1 // 1 = 1

print("Il resto dovuto é:", resto_dollari, "dollaro(i),", resto_quarter, "quarter,", resto_dime, "dime,", resto_nickel, "nickel,", resto_penny, "penny")



# O in alternativa: 

resto_dollari = resto_tot // dollaro                                        # In questo caso resto_dollari = 26 // 100 = 1
resto_quarter = (resto_tot % dollaro) // quarter                            # In questo caso resto_quarter = (126 % 100) // 25 = 1 
resto_dime = (resto_tot % dollaro % quarter) // dime                        # In questo caso resto_dime = (126 % 100 % 25) // 20 = 0
resto_nickel = (resto_tot % dollaro % quarter % dime) // nickel             # In questo caso resto_nickel = (126 % 100 % 25 % 20) // 5 = 0
resto_penny = (resto_tot % dollaro % quarter % dime % nickel) // penny      # In questo caso resto_nickel = (126 % 100 % 25 % 20 % 5) // 1 = 0


print("Il resto dovuto é:", resto_dollari, "dollaro(i),", resto_quarter, "quarter,", resto_dime, "dime,", resto_nickel, "nickel,", resto_penny, "penny")