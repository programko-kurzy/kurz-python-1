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