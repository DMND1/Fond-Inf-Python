# Realizzare una funzione che, ricevendo per parametro il nome di un file, restituisca una tripla con il numero di linee, 
# il numero di parole e il numero dei caratteri presenti nel file

nome = input("Nome file: ")

def funzione(nome):
    file = open(nome, "r")

    conta_linee = 0
    conta_parole = 0
    conta_caratteri = 0

    for linea in file:
        conta_linee += 1

        linea = linea.strip()
        conta_caratteri += len(linea)

        lista_linea = linea.split()
        conta_parole += len(lista_linea)

    file.close()

    return conta_linee, conta_parole, conta_caratteri


print(funzione(nome))