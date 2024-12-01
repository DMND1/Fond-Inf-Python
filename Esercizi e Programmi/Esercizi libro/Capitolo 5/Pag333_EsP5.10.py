# Scrivete la funzione def readFloat(prompt)
# che visualizzi la stringa prompt, seguita da uno spazio, poi acquisica un numero in virgola mobile e lo restituisca secondo il seguente utilizzo tipico:
# salary = readFloat("Please enter your salary:")
# percentageRaise = readFloat("What percentage reaise wuold you like?")

def readFloat(prompt):
    new_prompt = prompt + " "
    return float(input(new_prompt))

salary = readFloat("Please enter your salary:")
percentageRaise = readFloat("What percentage reaise wuold you like?")

print(salary)
print(percentageRaise)