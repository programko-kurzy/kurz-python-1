from random import randint
ran = str(randint(1, 10))


# Vyskúšajte
# Jednoduchý if, ktorý vždy vypíše „Číslo = 5“
cislo = 5
if cislo == 5:
    print('číslo = 5')
# if ktorý reaguje na input od užívateľa
slovo = input('zadajte slovo: ')
if slovo == 'auto':
    print('zadané slovo je auto')
else:
    print('zadané slovo nie je auto')

# Vyskúšajte
# Vyskúšajte si rôzne podmienky, aby ste si osvojili prácu s logickými operátormi, napríklad:
cislo = int(input('zadajte číslo: '))
if 3 < cislo < 5:
    print('zadané číslo je menšie 5')
    print('zadané číslo je väčšie ako 3')
else:
    print('zadané číslo je väčšie ako 3 a menšie ako 5')

cislo1 = int(input('zadajte číslo: '))
cislo2 = int(input('zadajte číslo: '))
if cislo1 == 5 and cislo2 == 5:
    print('obe čísla sú 5')
else:
    print('aspon jedno číslo nie je 5')

cislo1 = int(input('zadajte číslo: '))
cislo2 = int(input('zadajte číslo: '))
if cislo1 == 5 or cislo2 == 5:
    print('aspon jedno číslo je 5')
else:
    print('obe čísla nie sú 5')


# 4.1 Príklad
# Napíšte program, ktorý si od užívateľa vypýta slovo, uloží ho do premennej. Ak je slovo „voldemort“, vypíše „psst
# toto meno nesmieme vypisovať“.
slovo = input('Zadaj slovo: ')
if slovo == 'voldemort':
    print('psst toto meno nesmieme vypisovať')


# 4.2 Príklad
# Napíšte program, ktorý si od užívateľa vypýta dve slová (napríklad zadajte nové heslo a zopakujte heslo) ak sú
# slová rozdielne, vypíše „Heslá musia byť rovnaké“
heslo = input('Zadaj heslo: ')
zopakovane_heslo = input('Zopakuje heslo: ')
if heslo != zopakovane_heslo:
    print('Heslá musia byť rovnaké')


# 4.3 Príklad
# Napíšte program, ktorý si od užívateľa vypýta dve čísla. Ak je súčin týchto čísel väčší ako 1000, vypíše „ok.“, inak
# vypíše „nabudúce prosím zadajte väčšie čísla“.
# Pripomienka: aby sme so zadanými číslami mohli robiť matematické operácie, musíme ich najprv zmeniť zo stringu
# na int a to príkazom int(), teda: x = int(input(„Vaša správa“))
cislo1 = int(input('Zadaj prve cislo'))
cislo2 = int(input('Zadaj druhe cislo'))
if cislo1 * cislo2 > 1000:
    print('ok')
else:
    print('nabudúce prosím zadajte väčšie čísla')


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


