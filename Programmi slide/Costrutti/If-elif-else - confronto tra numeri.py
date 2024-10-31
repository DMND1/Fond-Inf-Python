m = int(input("Primo numero: "))

n = int(input("Secondo numero: "))

if n < m :
    print( n, " è minore di ", m)

elif n == m :
    print("I numeri sono uguali")

else:
    print(n,"è maggiore di ", m)

"""
if n < m :
    print( n, " è minore di ", m)
    
else: 
    if n == m :
        print("I numeri sono uguali")
    else: 
        print(n,"è maggiore di ", m)
"""

# In alternativa else : if ... : può essere scritto come elif: 