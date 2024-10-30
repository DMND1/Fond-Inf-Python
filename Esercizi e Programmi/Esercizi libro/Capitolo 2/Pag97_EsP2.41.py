# Il circuito qui raffigurato illustra gli aspetti più rilevanti della connesione esitente tra un'azienda che fornisce energia elettrica e uno dei suoi clienti. 
# Il cliente viene rappresentato da tre pararnetri: Vt, P e Pf. II parametro Vt è la tensione disponibile collegandosi a una presa a muro: i clienti si aspettano 
# di ottenere una tensione Vt affidabile, affinché i propri elettrodomestici funzionino correttamente, per cui le aziende distributrici regolano con particolare cura 
# tale parametro. P descrive la quantità di potenza usata dal cliente ed è il fattore principale nella determinazione della sua bolletta elettrica. Il fattore di 
# potenza, Pf, meno noto (viene calcolato come coseno di un angolo, per cui il suo valore è compreso tra zero e uno ??? [tra - 1 e 1]). In questo esercizio vi si chiede 
# di scrivere un programma Python che indaghi sul significato del fattore di potenza.

# Nella figura le linee elettriche sono rappresentate, in modo piuttosto semplificato, mediante resistenze, misurate in Ohm. Il modello dell'azienda elettrica è una 
# sorgente di tensione in corrente alternata (AC) e la tensione Vs necessaria per fornire al cliente la potenza P alla tensione Vt pub essere calcolata usando questa 
# formula (dove la tensione Vs ha Vrms come unità di misura):

# Vedi libro

# Da questa formula si evince che il valore di Vs, dipende dal valore di Pf. Scrivete un programma Python che chieda all'utente il valore del fattore di potenza e, poi, 
# visualizzi un messaggio contenente il valore di Vs corrispondente, usando i valori di P, R e Vt presenti nella figura.

from math import sqrt

P = 260     # W
R = 10      # Ohm
V_t = 120   # Vrms

pf = float(input("Il valore del fattore di potenza è: "))

V_s = sqrt((V_t + 2 * R * P / V_t)**2 + ( 2 * R * P / (pf * V_t))**2 + (1-pf**2))

V_s = round(V_s, 2)

print("Il risultato della tensione Vs é:", V_s)