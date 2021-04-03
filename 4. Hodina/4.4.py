from random import randint
ran = str(randint(1, 10))

# 4.4 Bonusový príklad - uhádni číslo
# S malo pomocou od externej knižnice si môžete vytvoriť jednoduchú hru „Uhádni číslo“
#
# Na začiatok kódu si napíšte tieto dva riadky:
# from random import randint
# ran = str(randint(1, 10))
# Tieto riadky najprv nahrajú funkciu randint z externej knižnice random ktorú následne použijeme aby sme
# vygenerovali číslo medzi 1 a 10 (môžete si čísla zmeniť na akékoľvek chcete), následne je toto číslo pretypované na
# string a uložené do premennej ran.
# Ako presnejšie ale fungujú na teraz nepotrebujete vedieť, dôležité je že nám táto funkcia vygeneruje náhodné číslo
# Čo chceme teraz spraviť je, vypýtať si od užívateľa číslo so správou „Hádaj číslo: “, pomocou
# podmienky zistiť či je zadané číslo rovnaké ako číslo v premennej „ran“, ak áno vypísať „Uhádli ste!“ inak vypísať
# „Neuhádli ste“
hadanie = int(input('Zadaj cislo: '))
if hadanie == ran:
    print('Uhádli ste!')
else:
    print('Neuhádli ste')