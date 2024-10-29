# Una banca online vi ha chiesto di progettare un programma che mostri ai potenziali clienti come aumenteranno i loro depositi. Il programma deve acquisire in ingresso
# il saldo iniziale e il tasso di interesse annuo (ma gli interessi vengono calcolati e accreditati mensilmente), per poi visualizzare il saldo dopo 3 mesi, 
# come in questo esempio di esecuzione: 

# Initial balance: 1000
# Annual intrest rate: 6.0
# After first month: 1005.00
# After second month: 1010.03
# After second month: 1015.08

saldo = int(input("Saldo iniziale: "))
interesse_annuo = float(input("Interesse annuo: "))


interesse_mensile = interesse_annuo / 12
# Interesse composto: saldo * (1 + interesse mensile / 100)**n dove n è il numero del mese

saldo_1_mese = saldo * (1 + interesse_mensile / 100)**1
saldo_2_mese = saldo * (1 + interesse_mensile / 100)**2
saldo_3_mese = saldo * (1 + interesse_mensile / 100)**3
saldo_1_anno = saldo * (1 + interesse_mensile / 100)**12

saldo_1_mese = round(saldo_1_mese, 2)
saldo_2_mese = round(saldo_2_mese, 2)   # 1010.024999 lo arrotonda a 1010.02 invece che 1010.03
saldo_3_mese = round(saldo_3_mese, 2)
saldo_1_anno = round(saldo_1_anno, 2)

print("Saldo dopo 1 mese:", saldo_1_mese)
print("Saldo dopo 2 mesi:", saldo_2_mese)
print("Saldo dopo 3 mesi:", saldo_3_mese)
print("Saldo dopo 1 anno:", saldo_1_anno)