# Un negozio di videonoleggio vuole premiare i propri clienti migliori con uno sconto basato sul numero di noleggi di film e sul numero di nuovi clienti che si sono
# registrati presso il negozio in seguito al suggerimento del cliente in esame. Lo sconto agisce come percentuale ed è uguale alla somma degli sconti dovuti ai noleggi
# e ai nuovi clienti, ma non può eccedere il 75 percento. Scrivete un programma che calcola il valore dello sconto, come in questo esempio di esecuzione:

# Enter the number of movie rentals: 56
# Enter the number of members refferred to the video club: 3
# The discount is equal to: 59.00 percent

n_noleggi = int(input("Numero di noleggi: "))
n_clienti = int(input("Numero di nuovi clienti: "))

sconto_iniziale = n_noleggi + n_clienti
sconto_finale = min(75, sconto_iniziale)

print("Lo sconto sarà:", sconto_finale)