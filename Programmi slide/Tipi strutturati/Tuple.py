##Tuple
#Sequenze immutabili di elementi, non si può cambiare nemmeno la posizione

parole = ("Noli", "me", "tangere")
cifre = 1, 7, 2, 9
print(cifre)    #(1, 7, 2, 9)
print(parole.index("me"))   #1
print(cifre[1:3])   #(7, 2)
print(sum(cifre))   #19

print(parole +  cifre)  #("Noli", "me", "tangere", 1, 7, 2, 9)
a, b, c, d = cifre
print(a)    #1

print(cifre[1])    #7
#stampa l'elemento 1 della tupla
print(cifre[1:2])   #(7,)
#stampa una sottotupla con un elemento

print("%3.1f, %3d, %3d, sono numeri" % (1.23, 2, 3))    #1.2, 2, 3 sono numeri

#assegnando una tupla a un nuovo valore si crea un nuovo nome per la stessa tupla

########################################################################################

stringa = "taoTaoTao"

print(stringa[1:7:2])   #aTo
#stampa da 1 a 6 ogni 2 caratteri
print(stringa[::-1])    #oaToaToaT
#stampa al contrariow