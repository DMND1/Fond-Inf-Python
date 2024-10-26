# Visualizzare una schiacchiera. Scrivete un programma che visualizzi una scacchiera per giocare a tris come questa:
# +--+--+--+
# |  |  |  |
# +--+--+--+
# |  |  |  |
# +--+--+--+
# |  |  |  |
# +--+--+--+

riga1 = "+--+--+--+"
riga2 = "|  |  |  |"

print(riga1 + "\n" + riga2 + "\n" + riga1 + "\n" + riga2 + "\n" + riga1 + "\n" + riga2 + "\n" + riga1)

# o in alternativa: 
print("\n")

riga1 = "+--+--+--+" + "\n" + "|  |  |  |"

print(riga1 + "\n"  + riga1 + "\n"  + riga1 + "\n" + riga1 + "\n" + "+--+--+--+")