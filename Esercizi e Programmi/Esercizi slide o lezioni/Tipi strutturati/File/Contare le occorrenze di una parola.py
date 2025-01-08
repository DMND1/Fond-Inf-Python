# Realizzare una funzione che conti le occorrenze di ogni parola presente in un file il cui nome è dato come parametro e le scriva su un altro file
# il cui nome è anch’esso dato come parametro

def funzione(nome_input, nome_output):
    file_input = open(nome_input, "r")
    file_output = open(nome_output, "w")

    tutto = file_input.read()
    tutto = tutto.split()
    file_input.close()

    dizionario = {}

    for parola in tutto:
        dizionario[parola] = tutto.count(parola)

    for chiave in dizionario:
        file_output.write(chiave + ": " + str(dizionario[chiave]) + "\n")

    file_output.close()

nome_input, nome_output = r"C:\Fond-Inf-Python\Risorse\Prove.txt", r"C:\Fond-Inf-Python\Risorse\Prove2.txt"

funzione(nome_input, nome_output)