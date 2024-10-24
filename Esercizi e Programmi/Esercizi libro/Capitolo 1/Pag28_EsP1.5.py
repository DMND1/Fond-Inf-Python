# programma che stampa il prorpio nome all'interno di un rettangolo come nell'esempio:
# +----+
# | ab |
# +----+

nome = input()

riga1 = "+" + "-" * ((len(nome))+2) + "+"
riga2 = "| " + nome + " |"

print(riga1)
print(riga2)
print(riga1)
