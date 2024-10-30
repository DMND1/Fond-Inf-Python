# Alcuni sensori di temperatura possono essere collegati direttamente ai tubl in rame per misurare la temperatura dei liquidi al loro interno. 
# Ciascun sensore contiene un disposlttvo a semiconduttore, detto termistore, che è caratterizzato da una resistenza dipendente dalla temperatura secondo la legge seguente:

# Vedi libro

# dove R è la resistenza (in Ohm) alla ternperatura T (in °K) e R0 la resistenza (in Ohm) alla temperatura T0 (in °K), mentre ß una costante che dipende dal materiale
# usato per fabbricare il termistore. In pratica, quindi, un termistore viene specificato mediante i suoi tre parametri, R0, T0 e ß. I termistori usati per i sensori 
# analizzati in questo esercizio hanno R0 = 1075 Ohm, T0 = 85 °C e ß = 3969 °K (si noti che il coefficiente espresso in °K e si ricordi che la temperatura in °K si ottiene 
# aggiungendo 273.15 alla temperatura espressa in °C). La temperatura del liquido, in °C, è determinata dalla resistenza R, espressa in Ohm, usando la formula seguente:

# Vedi libro

# Scrivete un progranuna Python che chieda all'utente la resistenza R del termistore e visualizzi un messaggio che riporti la temperatura del liquido, in °C.

from math import log

R_0 = 1075   # Ohm
T_0 = 85     # °C, da convertire in Kelvin
B = 3969     # °K

T_0_Kelvin = T_0 + 273.15

R = float(input("Resistenza del termistore: "))

T_Celsius = B * T_0_Kelvin / (T_0_Kelvin * log(R / R_0) + B) - 273.15  # Il - 273.15 indica che la conversione da Kelvin a Celsius è già nella formula

T_Celsius = round(T_Celsius, 2)

print("La temperatura del liquido è:", T_Celsius, "°C")