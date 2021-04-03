# 4.2 Príklad
# Napíšte program, ktorý si od užívateľa vypýta dve slová (napríklad zadajte nové heslo a zopakujte heslo) ak sú
# slová rozdielne, vypíše „Heslá musia byť rovnaké“
heslo = input('Zadaj heslo: ')
zopakovane_heslo = input('Zopakuje heslo: ')
if heslo != zopakovane_heslo:
    print('Heslá musia byť rovnaké')