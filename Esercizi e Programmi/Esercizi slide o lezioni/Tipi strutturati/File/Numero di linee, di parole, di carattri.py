# Realizzare una funzione che, ricevendo per parametro il nome di un file, restituisca una tripla con il numero di linee, il numero di parole e il 
# numero dei caratteri presenti nel file

# Contare le righe
nome_file = "Esercizi e Programmi\Esercizi slide o lezioni\Tipi strutturati\File\parole.txt"


def contaRighe(nome_file):
    num_linee = 0
    num_caratteri = 0
    file = open(nome_file, "r")

    for linea in file:
        num_linee += 1

    file.close()

    return num_linee, num_caratteri

print(contaRighe(nome_file))