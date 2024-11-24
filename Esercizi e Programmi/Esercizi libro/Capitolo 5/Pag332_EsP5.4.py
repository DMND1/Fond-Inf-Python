# Scrivete la funzione: def middle(string)
# che restituisca il carattere centrale di string se la lunghezza di stringa è dispari, o i due caratteri centrali sela lunghezza di stringa è pari

# ciao
# len(ciao) = 4
# 4 / 2 = 2
# stampa s[1:3]

# cia
# len(cia) = 3
# 3 // 2 = 1
# stampa s[1]

def middle(string):
    if string == "":        # analogo a: if len(string) == 0:
        return None
    elif len(string) % 2 == 0:
        estremo = len(string) // 2 - 1
        return string[estremo : estremo + 2]
    else:
        estremo = len(string) // 2
        return string[estremo]

print(middle(""))
print(middle("Middle"))
print(middle("Una"))