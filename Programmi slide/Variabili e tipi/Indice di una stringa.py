saluto = "SALVE"

print(saluto[1] + saluto[3] + saluto[4]) # stampa: AVE

print(saluto[1:4]) # stampa: ALV

print(saluto[1:len(saluto)]) # stampa dal carattire di posizione 1 fino all'ultimo carattere: ALVE
print(saluto[1:]) # altro modo per eseguiro lo stesso comamdo
print(saluto[:-1])

ultimo = len(saluto) - 1 # indice dell'ultimo carattere

print(saluto[ultimo]) # stampa: E

saluto[0] = "s" # da errore, le stringe sono costanti, le singole cifre non possono essere cambiate