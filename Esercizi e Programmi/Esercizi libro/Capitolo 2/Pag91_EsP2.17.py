# Scrivete un programma che legga due orari in formato militare (ad esempio, 0900 o 1730) e visualizzi il numero di ore e di minuti che li separano nel tempo

# Esempio 2: 
# Primo orario: 0900
# Secondo orario: 1730
# Risultato: 8 ore e 30 minuti

# Esempio 2:
# Primo orario: 1730
# Secondo orario: 0900
# Risultato: 15 ore e 30 minuti

orario_1 = input("Primo orario: ")
orario_2 = input("Secondo orario: ")

# Esempio 1: 
# 1730 - 0900 = 8 ore e 30 minuti
# 17-9 = 8 ore
# 30-0 = 30 minuti
# 2400 + 0830

# Esempio 2:
# 0900 - 1730 = - 8 ore e - 30 minuti
# 9-17 = - 8 ore
# 0-30 = - 30 minuti
#
# 2400 - 0830 = 15 ore e 30 minuti
#
# 2400 - (1730 - 0900) = 24 ore - (8 ore e 30 minuti) = 15 ore e 30 minuti

# Non saprei come implementare un dingolo programma che riesca a dare un risultato in entrambi i casi