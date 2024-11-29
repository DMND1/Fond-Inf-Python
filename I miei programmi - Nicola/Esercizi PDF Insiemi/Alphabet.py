def controllo(stringa):
    stringa = stringa.replace(" ","")
    alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"}
    for i in alphabet:
        if i not in stringa:
            return True
    
    return False


stringa = input("Inserisci una frase da controllare: ")

if controllo(stringa) == True:
    print("Non ci sono tutte le lettere baka")
else:
    print("E ti ci sei pure impegnato")