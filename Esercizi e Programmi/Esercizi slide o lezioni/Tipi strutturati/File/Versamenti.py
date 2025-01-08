# Un file contiene per ogni riga il nome di una persona e una cifra (numero intero) in euro rappresentante un versamento. 
# Un nome di una persona può ripetersi più volte. Realizzare un programma che per ogni nome di persona stampi la somma dei versamenti di quella persona.

nome = r"C:\Fond-Inf-Python\Risorse\Prove3txt"
file = open(nome, "r")

dizionario = {}

for linea in file:
    linea = linea.split()
    dizionario[linea[0]] = dizionario.get(linea[0], 0) + int(linea[1])

for chiave in dizionario:
    print(chiave + " deve versare: " + str(dizionario[chiave]) + " euro")