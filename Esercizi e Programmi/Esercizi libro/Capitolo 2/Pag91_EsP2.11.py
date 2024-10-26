# Scrivere un programma che chieda all'utente di fornire: 
# - Il numero di galloni di carburante presenti nel serbatoio
# - L'efficienza del motore in miglia percorse per gallone
# - Il costo del carburante (in dollari per gallone)
# Poi visualliza la spesa necessaria per percorrere 100 miglia e la distanza percorribile con il carburante rimasto ancora nel serbatoio


carburante = float(input("Numero di galloni di carburante presenti nel serbatoio: "))
eff_motore = float(input("Efficienza del motore in miglia percorse per gallone: "))
costo_carburante = float(input("Costo carburante per un gallone: "))

spesa_100_miglia = (100 / eff_motore - carburante) * costo_carburante 
miglia_carburante = eff_motore * carburante

print("Spesa necessaria per percorrere 100 miglia:", spesa_100_miglia)
print("Distanza percorribile con il carburante rimasto:", miglia_carburante)
