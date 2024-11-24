# Scrivete un programma che acquisisca numeri in ingresso e li aggiunga ad una lista, se non sono già presenti al suo interno. 
# Quando la lista contiene dieci numeri, il programma li visualizza e termina.

lista = []

while len(lista) != 10:
    x = int(input("Inserire un numero: "))
    if not(x in lista):
        lista.append(x)
    
print(lista)