# 8.6 Príklad
# Užívateľ zadá slovo. Pomocou for cyklu potom skontrolujte či sú všetky písmená v slove rovnaké
# a vypíšte či áno alebo nie.
slovo = input('Zadaj slovo: ')
je_rovnake = True
for i in range(1, len(slovo)):
    if je_rovnake and slovo[0] != slovo[i]:
        je_rovnake = False

if je_rovnake:
    print('ano, vsetko pismena su rovnake')
else:
    print('nie, vsetky pismena nie su rovnake')