n = int(input("Un numero: "))

if n < 0 :
    n = -n  #cambio del segno

# Si può omettere il seguente, infatti se viene omesso allora questa operazione viene eseguita automoaticamente:
else: 
    pass

print("Il valore assoluto è:", n)