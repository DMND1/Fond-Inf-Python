# A = voto tra 28 e 30
# A- = 28
# A = 29
# A+ = 30
# B = voto tra 25 e 27
# C = voto tra 22 e 24
# D = voto tra 19 e 21

# Il programma chiede un voto in lettera (nel sistema anglosassone, per es: C+) e lo converte in voto in trentesimi, per poi stamparlo

# leggi voto
# se il voto è A allora:
#   se c'è + allora:
#       risultato = 30
#   e c'è - allora:
#       risultato = 28
#   altrimenti = 29
# ...

# Es: voto = "A+", risultato: 30

voto = input("Il voto nel sistema anglosassone é: ")

if voto[0] == "A":
    if len(voto) == 2 and voto[1] == "+":
        risultato = 30
    elif len(voto) == 2 and voto[1] == "-":
        risultato = 28
    else:
        risultato = 29

elif voto[0] == "B":
    if len(voto) == 2 and voto[1] == "+":
        risultato = 27
    elif len(voto) == 2 and voto[1] == "-":
        risultato = 25
    else:
        risultato = 26

elif voto[0] == "C":
    if len(voto) == 2 and voto[1] == "+":
        risultato = 24
    elif len(voto) == 2 and voto[1] == "-":
        risultato = 22
    else:
        risultato = 23

elif voto[0] == "D":
    if len(voto) == 2 and voto[1] == "+":
        risultato = 21
    elif len(voto) == 2 and voto[1] == "-":
        risultato = 19
    else:
        risultato = 20

print("Il voto in trentesimi è:", risultato)