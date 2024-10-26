# Programma che chiede all'utente una misura espressa in metri e la converte in miglia, piedi e pollici

x = float(input("Misura in metri: "))

miglia = round(x * 0.000621371 , 5)
piedi = round(x * 3.28084 , 2)
pollici = round(x * 39.3701 , 2)

print("La misura in miglia é:", miglia)
print("La misura in piedi è:", piedi)
print("La misura in pollici é:", pollici)