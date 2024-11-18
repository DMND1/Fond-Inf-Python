# Un anno di 366 giorni viene detto bisestile (leap) e serve a mantenere il calendario sincronizzato con il Sole, dal momento che la Terra vi ruota attorno una volta 
# ogni 365.25 giorni. In realtà questo numero non è esatto, e per tutte le date successive al 1582 si applica la correzione gregoriana: solitamente gli anni divisibili 
# per 4, come il 1996, sono bisestili, ma gli anni divisibili per 100 come il 1900, non lo sono; come eccezione all'eccezione, gli anni divisibili per 400, come il 2000, 
# sono bisestili. Scrivete un progratnrna che chieda all'utente un anno e determini se si tratta di un anno bisestile, usando un unico enunciato if.

anno = int(input("Inserire un anno: "))

# Se l'anno viene dopo il 1582
anno_gregoriano = (anno > 1582)
# Se l'anno è divisibile per 4
divisibile_per_4 = (anno % 4 == 0)
# Se l'anno è divisibile per 100
divisibile_per_100 = (anno % 100 == 0)
# Se l'anno è divisibile per 400
divisibile_per_400 = (anno % 400 == 0)

if ((not anno_gregoriano) and divisibile_per_4) or (anno_gregoriano and divisibile_per_4 and ((not divisibile_per_100) or divisibile_per_400)):
    print("L'anno è bisestile")
else: 
    print("L'anno non è bisestile")