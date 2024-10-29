# Il punto di riudiada T_d (in inglese dew point) può essere approssimativamente calcolato a partire dall'umidità relativa, RH, e dalla temperatura effettiva, T, 
# con queste formule, dove a = 17.27 e b = 237.7 °C

# Vedi libro per formula

# Scrivere un programma che acquisisca in ingresso l'umidità relativa (0<RH<1) e la temperatura (In gradi Celsius), visualizzando di conseguenza il punto di rugiada.
# Per calcolare il ln usate la funzione python log

from math import log

RH = float(input("Umidità relativa (0<RH<1): "))
T = float(input("Temperatura (°C): "))

a = 17.27
b = 237.7

f_T_RH = a * T / (b + T) + log(RH)

T_d = b * f_T_RH / (a - f_T_RH)
T_d = round(T_d, 2)

print("Il punto di rugiada è:", T_d)