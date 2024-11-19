# Letta una stringa verificare se ci sono caratteri ripetuti e stampare il carattere ripetuto e per quante volte

s1 = input("Inserire la stringa 1: ")

# Per ogni lettera in s1
for i in s1:
    # Reset variabili
    cont = 0
    # Per ogni lettera in s1
    for c in s1:
        # Se due lettere sono uguali
        if c == i:
            # Aumenta il contatore
            cont += 1
    # Rimuovo la lettera dalla parola per evitare di ripetere conti
    s1 = s1.replace(i,"")
    # Se il contatore non è 0, questo poiché nel primo for s1 rimane invariata
    if cont != 0:
        # Stampa quante volte la lettera si ripete nella stringa
        print("La lettera", i, "si ripete", cont, "volte")