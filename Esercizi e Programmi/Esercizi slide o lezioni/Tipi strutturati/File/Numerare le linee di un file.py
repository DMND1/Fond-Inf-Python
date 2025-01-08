# Realizzare una funzione che, ricevendo come parametri i nomi di un file di input ed uno di output, numeri le linee del file di input e le scriva nel file di output

def funzione(nome_input, nome_output):
    file_input = open(nome_input, "r")
    file_output = open(nome_output, "w")

    contatore_linee = 1
    for linea in file_input:
        file_output.write(str(contatore_linee)+ " " + linea)
        contatore_linee += 1
    
    file_input.close()
    file_output.close()
    

nome_input, nome_output = r"C:\Fond-Inf-Python\Risorse\Prove.txt", r"C:\Fond-Inf-Python\Risorse\Prove2.txt"

funzione(nome_input, nome_output)