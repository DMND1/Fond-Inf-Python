# Scrivete un programma che traduca un voto in lettere nel corrispondente voto numerico. I voti in lettere sono A, B, C, D e F, eventualmente seguiti da un segno + o -. I loro
# valori numerici sono, nell'ordine, 4, 3, 2, 1, 0. I voti F+ e F- non esistono. Un segno + aumenta il voto numerico di 0.3, mentre un segno - lo diminuisce della stessa quantità.
# Il voto A+ è comunque uguale a 4.0

voto = input("Il voto nel sistema anglosassone é: ")

A = 4.0
B = 3.0
C = 2.0
D = 1.0
F = 0

if voto[0] == "A":
    if len(voto) == 2 and voto[1] == "+":
        risultato = A
    elif len(voto) == 2 and voto[1] == "-":
        risultato = A - 0.3
    else:
        risultato = A

elif voto[0] == "B":
    if len(voto) == 2 and voto[1] == "+":
        risultato = B + 0.3
    elif len(voto) == 2 and voto[1] == "-":
        risultato = B - 0.3
    else:
        risultato = B

elif voto[0] == "C":
    if len(voto) == 2 and voto[1] == "+":
        risultato = C + 0.3
    elif len(voto) == 2 and voto[1] == "-":
        risultato = C - 0.3
    else:
        risultato = C

elif voto[0] == "D":
    if len(voto) == 2 and voto[1] == "+":
        risultato = D + 0.3
    elif len(voto) == 2 and voto[1] == "-":
        risultato = D - 0.3
    else:
        risultato = D

elif voto[0] == "F":
    if len(voto) == 2 and voto[1] == "+":
        risultato = "il voto nel sistema anglosassone non esiste"
    elif len(voto) == 2 and voto[1] == "-":
        risultato = "il voto nel sistema anglosassone non esiste"
    else:
        risultato = F

print("Il voto convertito è:", risultato)