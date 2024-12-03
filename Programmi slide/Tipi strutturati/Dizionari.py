Temperature = { "Chieti":21, "L'Aquila":18, "Pescara":22, "Teramo":20 }

print(Temperature[Pescara])     # Da errore, Pescara non è definita come variabile
print(Temperature["Pescara"])   # Stampa 22

print(Temperature["Ascoli"])    # Da errore, la chiave "Ascoli" non esiste

Temperature["Ascoli"] = 30
print(Temperature["Ascoli"])    # ora stampa 30

print(len(Temperature))         # Stampa 5

Temperature["Pescara"] = 28
print(Temperature)

AltreTemperature = Temperature  # Sono lo stesso dizionario
print(Temperature)

Temperature["Chieti"] = 20
print(AltreTemperature)

CopiaTemperature = dict(Temperature)    # Copia di Temperature, sono due dizionari diversi
CopiaTemperature["Chieti"] = 50

print(CopiaTemperature)
print(AltreTemperature)



vuoto = dict()
print({} == vuoto)              # Stampa True

Studenti = dict()

Studenti[298654] = "Matteo"

print(Studenti)

Studenti[298721] = "Simona"
Studenti[300201] = "Irene"
Studenti[123145] = "Giorgia"

print(Studenti)



# Metodo values e metodo keyy
Quadrati = { -2: 4, 1: 1, 2: 4, 9: 81 }

print(list(Quadrati.values()))  # Stampa [1, 4, 4, 81]
print(list(Quadrati.keys()))    # Stampa [-2, 1, 2, 9]



Esami = {}

Esami[298654] = 0
Esami[298721] = 0

Esami[298654] = Esami[298654] + 1
Esami[298654] = Esami[298654] + 1

Esami[300201] = Esami[300201] + 1   # Da errore, il nuemero matricola 300201 non c'è come chiave nel dizionario

print(Esami)

# Metodo get
print(Esami.get(298654))    # Stampa 2

print(Esami.get(300201))    # Ritorna None se la chiave non esiste nel dizionario

print(Esami.get(300201, 0)) # Stampa il secondo paramentro se la chiave non esiste nel dizionario

# Esempio
Esami[300201] = Esami.get(300201, 0) + 1        # Assegna 0 + 1 =  1 alla chiave 300201

print(Esami)

