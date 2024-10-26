# Scrivere un programma che visualizzi le dimensioni in millimetri di un foglio di carta in formato "letter" (8.5 x 11 pollici, un pollice = 25,4 millimetri)

pollice = 25.4                                          # 25.4 mm

larghezza = round(pollice * 8.5, 1)
altezza = pollice * 11

print("La larghezza del foglio è:", larghezza, "mm")
print("L'altezza del fogliuo è: ", altezza, "mm")

