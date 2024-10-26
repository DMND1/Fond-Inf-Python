# Scrivete un programma che legga un numero compreso tra 10000 e 99999, dopo averlo chiesto all'utente, il quale inserirà il numero usando la virgola per separare 
# le migliaia, secondo l'uso anglosassone (esempio 10,000 oppure 99,999). Poi, visualizzate il numero senza la virgola. 

x = input("Selezionare un intero compreso tra 10,000 e 99,999: ")

x_stringa = str(x) # "11,111"

print ("Il numero senza virgola è:", x_stringa[0] + x_stringa[1] + x_stringa[3] + x_stringa[4] + x_stringa[5])

# in alternativa: 

x = str(input("Selezionare un intero compreso tra 10,000 e 99,999: "))

print ("Il numero senza virgola è:", x[0] + x[1] + x[3] + x[4] + x[5])