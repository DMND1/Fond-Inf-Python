primalista = ["Dario", "Giorgia", "Simona", "Matteo"]
secondalista = ["Irene", "Alessio", "Damiano", "Damiano"]

primalista[3] = "Mario"    # sostituisce matteo con Mario

secondalista = primalista

print(secondalista) # Stampa:
["Dario", "Giorgia", "Simona", "Matteo"]

print(primalista) # Stampa:
["Dario", "Giorgia", "Simona", "Matteo"]

primalista[3] = "Lucia"

print(primalista) # Stampa:
["Dario", "Giorgia", "Simona", "Lucia"]

print(secondalista) # Stampa:
["Dario", "Giorgia", "Simona", "Lucia"]

l1 = [1,2,3]
l2 = [1,2,3]

l1[2] = 4

print(l1) # Stampa:
[1,2,4]

print(l2) # Stampa:
[1,2,3]

l1 = [1,2,3]
l2 = [1,2,3]

# l1 e l2 sono due liste diverse ma con gli stessi valori
print(l1 == l2) # Stampa:
True

# secondalista e primalista sono la stessa lista
print(secondalista == primalista) # Stampa:
True

# E' importante la sequenza
l2 = [2,1,3]

print(l1 == l2) # Stampa:
False

# Ordinamento lessicografico
print(l1 < l2) # Stampa:
True