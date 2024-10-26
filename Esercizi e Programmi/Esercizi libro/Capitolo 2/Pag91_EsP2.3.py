# Scrivere un programma che visualizzi un numero, il suo quadrato, il cubo e la quarta potenza. Per calcolare la quarta potenza usare soltanto l'operatore **

x = float(input("Scegliere un numero: "))

quadrato = x ** 2
cubo = x ** 3
quarta_pot = x ** 4

print("Il numero scelto è:", x, "\n" + "Il suo quadrato vale:", quadrato, "\n" + "Il suo cubo vale:", cubo, "\n" + "La sua quarta potenza vale:", quarta_pot)