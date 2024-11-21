def righe(car, num_car = 20):   # scrivendo num_car = 20    stiamo dando come parametro di default 20 a num_car, num_car prenderà 
                                # questo valore se non c'è il secondo input
    print(car * num_car)
    print(car * num_car)

righe("-")  # assegna "-" a car e lo stampa 20 volte

def righe(car = "-", num_car = 20):
    print(car * num_car)
    print(car * num_car)

righe(30)   # ossia car = 30    quindi stamperà il risultato di 30 * 20
righe(num_car = 30) # assegna a num_car 30 e stamperà quindi "-" ripetuto 30 volte