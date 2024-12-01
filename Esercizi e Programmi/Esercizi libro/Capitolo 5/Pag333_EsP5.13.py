# Scrivete una funzione, getTimeName(hours, minutes)
# che restituisca il nome, in inglese, di un istante di tempo, come "ten minutes past two", "half past three", "a quarter to four", "five o'clock". 
# Ipotizzate che il valore hours sia compreso tra 1 e 12

# se i minuti > 30:
#   addiziona 1 alle ore
#   calcola i minuti rimanente alla prossima ora: 60 - minuti
# altrimenti se i minuti = 30:
#   nome dei minuti = half
# altrimentis se i minuti

# converti le ore nel loro nome in inglese
# converti i minuti nel loro nome in inglese

def getHoursName(hours):
    if hours == 1: 
        return "one"
    elif hours == 2: 
        return "two"
    elif hours == 3: 
        return "three"
    elif hours == 4: 
        return "four"
    elif hours == 5: 
        return "five"
    elif hours == 6: 
        return "six"
    elif hours == 7: 
        return "seven"
    elif hours == 8: 
        return "eight"
    elif hours == 9: 
        return "nine"
    elif hours == 10: 
        return "ten"
    elif hours == 11: 
        return "eleven"
    elif hours == 12: 
        return "twelve"


def getMinutesName(minutes):
    if minutes == 1: 
        return "one minute"
    elif minutes == 2: 
        return "two minutes"
    elif minutes == 3: 
        return "three minutes"
    elif minutes == 4: 
        return "four minutes"
    elif minutes == 5: 
        return "five minutes"
    elif minutes == 6: 
        return "six minutes"
    elif minutes == 7: 
        return "seven minutes"
    elif minutes == 8: 
        return "eight minutes"
    elif minutes == 9: 
        return "nine minutes"
    elif minutes == 10: 
        return "ten minutes"
    elif minutes == 11: 
        return "eleven minutes"
    elif minutes == 12: 
        return "twelve minutes"
    elif minutes == 13: 
        return "thirteen minutes"
    elif minutes == 14: 
        return "fourteen minutes"
    elif minutes == 15: 
        return "a quarter"
    elif minutes == 16: 
        return "sixteen minutes"
    elif minutes == 17: 
        return "seventeen minutes"
    elif minutes == 18: 
        return "eighteen minutes"
    elif minutes == 19: 
        return "nineteen minutes"
    elif minutes == 20: 
        return "twenty minutes"
    elif minutes == 21: 
        return "twenty-one minutes"
    elif minutes == 22: 
        return "twenty-two minutes"
    elif minutes == 23: 
        return "twenty-three minutes"
    elif minutes == 24: 
        return "twenty-four minutes"
    elif minutes == 25: 
        return "twenty-five minutes"
    elif minutes == 26: 
        return "twenty-six minutes"
    elif minutes == 27: 
        return "twenty-seven minutes"
    elif minutes == 28: 
        return "twenty-eight minutes"
    elif minutes == 29: 
        return "twenty-nine minutes"
    elif minutes == 30: 
        return "half"


def getTimeName(hours, minutes):
    if minutes == 0:
        return getHoursName(hours) + " o'clock"
    elif minutes > 30:
        hours += 1
        minutes = 60 - minutes
        return getMinutesName(minutes) + " to " + getHoursName(hours)
    elif minutes <= 30:

        minutes_name = getMinutesName(minutes)
        if minutes_name[0:2] == "a ":
            minutes_name = minutes_name[2:]
        
        return minutes_name + " past " + getHoursName(hours)



print(getTimeName(10, 0))   # Stampa: ten o'clock
print(getTimeName(9, 45))   # Stampa: a quarter to ten
print(getTimeName(9, 47))   # Stampa: thirteen minutes to ten
print(getTimeName(11, 15))  # Stampa: quarter past eleven
print(getTimeName(11, 30))  # Stampa: half past eleven
print(getTimeName(11, 13))  # Stampa: thirteen minutes past eleven