print('Ciao', "Mondo!" )

poeta = "D'Annunzio"   #notare l'apice interno alla stringa

lunghezza = len(poeta) #lunghezza vale 10

nome = "Gabriele" 

cognome = "D'Annunzio"   

poeta = nome + " " + cognome

print(poeta)  # stampa: Gabriele D'Annunzio

filosofo = "Bertrand Russell" 

maiuscolo = filosofo.upper() # assegna "BERTRAND RUSSELL" a maiuscolo

print(filosofo.lower())      # stampa: bertrand russell

figlio = filosofo.replace("Bertrand", "Conrad") # figlio vale "Conrad Russell"

print(figlio)

saluto = "SALVE" 

print(saluto[1] + saluto[3] + saluto[4]) #stampa: AVE

ultimo = len(saluto) - 1     #indice dell'ultimo carattere

print(saluto[ultimo])        #stampa: E
