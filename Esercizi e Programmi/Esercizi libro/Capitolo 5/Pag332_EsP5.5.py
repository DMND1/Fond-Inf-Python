# Scrivete la funzione: def repeat(string, n, delim)
# che ripete la stringa n volte, con le ripetizioni separate dalla stringa delim

def repeat(string, n, delim):
    if n == 0:
        return ""
    elif n > 0:
        string_and_delim = string + delim
        result = string_and_delim * (n-1) + string
        return result
    else:
        return None

print(repeat("Ciao", 0, ", "))
print(repeat("Ciao", 4, ", "))
print(repeat("Ciao", -1, ", "))