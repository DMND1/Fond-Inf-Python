# Creare una tabella che rappresenti una scacchiera. Le caselle vuote sono rappresentate dal carattere spazio, mentre ’P’, ’R’, ’D’, ’A’, ’C’ e ’T’ rappresentano 
# pedone, re, donna, alfiere, cavallo e torre per i bianchi. Usare le minuscole per i neri.

def vuota(n, m):
    matrice = []

    for i in range(n):
        riga = ["☐"] * m
        matrice.append(riga)

    return matrice


def creazioneScacchiera():
    scacchiera = vuota(8,8)

    riga1 = ["t","c","a","d","r","a","c","t"]
    riga_pedoni = ["p"] * 8

    scacchiera[0] = riga1
    scacchiera[1] = riga_pedoni

    copia_riga1 = list(riga1)
    copia_riga_pedoni = list(riga_pedoni)

    for i in range(len(copia_riga1)):
        copia_riga1[i] = copia_riga1[i].upper()
        copia_riga_pedoni[i] = copia_riga_pedoni[i].upper()
    
    scacchiera[6] = copia_riga_pedoni
    scacchiera[7] = copia_riga1

    return scacchiera

scacchiera = creazioneScacchiera()

for riga in scacchiera:
    for elem in riga:
        print(elem, end=" ")
    print()