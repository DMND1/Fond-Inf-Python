# Scrivete un programma per tradurre i numeri da 1 a 12 nei nomi dei mesi corrispondenti, in inglese: 
# January, February, March, April, May, June, July, August, September, October, November, December

# input 1
# output January
# output = mesi[0:9]

# input 2
# output February
# output = mesi[9:18]

# input 3
# output February
# output = mesi[18:27]

x = int(input("Numero del mese: "))

mesi = "January  February March    April    May      June     July     August   SeptemberOctober  November December "

output = mesi[(x-1)*9:x*9]
mese_fin = output.replace(" ","")   # In alternativa come suggerisce anche il libro si può usare la funzione strip: mese_fin = out.strip("")

print("Il mese corrispondente al numero scelto è:", mese_fin)
