""" 
Liste
"""

[1934, 1938, 1982, 2006] # lista di numeri interi

["rosa", "raso", "orsa"] # lista di stringhe

[ ]                      # lista vuota


frase = ['Era', 'una', 'notte', 'bulla', 'e', 'tempestosa'] 

voti = [18, 26, 30, 24, 27]  

temperature = [16.0, 17.2, 18.1, 19.5, 20.7, 20.3, 19.4, 17.9, 15.6]


print (voti[2])     # stampa 30

print (frase[3])    # stampa 'bulla'

frase[3] = 'buia'

voti[0] = 30

esamiSostenuti = len(voti) # esamiSostenuti vale 5

print ( len(temperature) ) # stampa 9


for i in range(9) :        # i assume tutti i valori tra 0 e 8
  print(i, temperature[i]) # stampa dell'indice e del valore associato

for i in range( len(temperature) ) : # stesso comportamento di sopra
  print(i, temperature[i]) 
  
  

for elemento in temperature : # elemento assume tutti i valori 
  print( elemento )           # stampa ogni elemento


articoli = []            # lista vuota!
print(articoli)

articoli.append("il")    # ["il"]
articoli.append("la")    # ["il", "la"]
print(articoli)

articoli.insert(1, "lo") # ["il","lo", "la"] inserimento in posizione 1
print(articoli)

articoli.pop(2)          # ["il","lo"] rimosso elemento in posizione 2
print(articoli)

articoli.remove("il")    # ["lo"]  rimozione senza sapere la posizione

tutti = ["il","lo", "la", "i","gli", "le"] 


a = tutti.index("gli")   # a vale 4
print(a)


plurali_maschili = tutti[3:5] # plurali_maschili vale ["i","gli"]
print(plurali_maschili)

tutti.sort()             # 

print(tutti)

print([1,2] <= [1.0,2,1])


valori = [22, 11, 34, 17, 52 , 26, 13]

print ( sum( valori ) )    # stampa 
print ( min( valori ) )
print ( max( valori ) )

c = list("ciao")           # ["c", "i", "a", "o"]

copia = list( c )          # anche copia vale ["c", "i", "a", "o"] 
                           # ma è un'altra lista
                           
pari = list(range(0,10,2)) # pari vale [0, 2, 4, 6, 8]

print (c, copia, pari)