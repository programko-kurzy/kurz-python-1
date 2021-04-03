# 8.1 Príklad
# Vypýtajte si od užívateľa dve slová pomocout input()
# a následne ich vypíšte vedľa seba do riadku.
slovo1 = input('Zadaj prve slovo: ')
slovo2 = input('Zadaj druhe slovo: ')
print(slovo1, slovo2)


# 8.2 Príklad
# Vypýtajte si od užívateľa dve čísla pomocout input()
# a následne vypíšte pod seba ich: súčet, rozdiel, súčin.
cislo1 = int(input('Zadaj prve cislo: '))
cislo2 = int(input('Zadaj druhe cislo: '))
print('Sucet:', cislo1 + cislo2)
print('Rozdiel:', cislo1 - cislo2)
print('Sucin:', cislo1 * cislo2)


# 8.2.1 Príklad
# Vylepšite príklad 8.2 tak, že pre každú operáciu si vytvoríte samostatnú funkciu.
def sucet():
    cislo1 = int(input('Zadaj prve cislo: '))
    cislo2 = int(input('Zadaj druhe cislo: '))
    print('Sucet:', cislo1 + cislo2)


def rozdiel():
    cislo1 = int(input('Zadaj prve cislo: '))
    cislo2 = int(input('Zadaj druhe cislo: '))
    print('Rozdiel:', cislo1 - cislo2)


def sucin():
    cislo1 = int(input('Zadaj prve cislo: '))
    cislo2 = int(input('Zadaj druhe cislo: '))
    print('Sucin:', cislo1 * cislo2)


# 8.3 Príklad
# Vypýtajte si od užívateľa číslo a následne toľko krát (pomocou for cyklu)
# vypíšte ľubovoľné slovo.
n = 5
cislo = int(input('Zadaj cislo: '))
for i in range(cislo):
    print(n)


# 8.4 Bonusový príklad
# Spojte úlohy 8.3 a 8.2.1, teda:
# Užívateľ zadá číslo, spustí sa for cyklus toľko krát ako zadané číslo
# a v každom cykle si program vypýta dve čísla a vykoná s nimi matematické
# operácie rovnako ako v úlohe 8.2.1
def sucet(cislo1, cislo2):
    print('Sucet:', cislo1 + cislo2)


def rozdiel(cislo1, cislo2):
    print('Rozdiel:', cislo1 - cislo2)


def sucin(cislo1, cislo2):
    print('Sucin:', cislo1 * cislo2)


cislo = int(input('Zadaj cislo: '))
for i in range(cislo):
    cislo1 = int(input('Zadaj cislo: '))
    cislo2 = int(input('Zadaj cislo: '))
    sucet(cislo1, cislo2)
    rozdiel(cislo1, cislo2)
    sucin(cislo1, cislo2)


# 8.5 Príklad
# Užívateľ zadá slovo. Ak je toto slovo „leto“ program vypíše: „oh, na to sa teším“, inak
# vypíše „jediné na čo sa teším je leto..“
slovo = input('Zadaj slovo: ')
if slovo == 'leto':
    print('oh, na to sa teším')
else:
    print('jediné na čo sa teším je leto..')


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


# 8.7 Bonusový príklad
# Úloha 8.7 sa dá spraviť aj bez for cyklu, oveľa jednoduchšie. Porozmýšľajte ako a vyskúšajte
# ju zjednodušiť.
slovo = input('Zadaj slovo: ')
if len(slovo) == 0:
    print('Slovo je prazdne')
elif slovo[0] == slovo[-1]:  # to iste ako elif slovo[0] == slovo[len(slovo) - 1]
    print('Ano, prve a posledne pismeno su rovnake')
else:
    print('Nie, prve a posledne pismenu nie su rovnake')


# 8.8 Príklad
# Vytvorte funkciu sucetAleboSucin, ktorá dostane dve čísla, tie vynásobí a ak je súčin menší ako 1000,
# vráti ho, inak vráti namiesto neho ich súčet
def sucetAleboSucin(cislo1, cislo2):
    sucin = cislo1 * cislo2
    if sucin < 1000:
        return sucin
    return cislo1 + cislo2


# 8.9 Príklad
# Vytvorte funkciu parnePismena, ktorá dostane jedno slovo, a vypíše iba
# písmená na párnych pozíciách
# Príklad: slovo = „Ahoj“
# Výpis: „Ao“ (pozície začínajú od nula, ale aj výstup „hj“ by bol správny)
def parne_pismena(slovo):  # pre Ao
    for i in range(0, len(slovo), 2):
        print(slovo[i], end='')


def parne_pismena(slovo):  # pre hj
    for i in range(1, len(slovo), 2):
        print(slovo[i], end='')


def parne_pismena_lepsie(slovo):  # pre Ao
    print(slovo[::2])


def parne_pismena_lepsie(slovo):  # pre hj
    print(slovo[1::2])


# 8.10 Bonusový príklad
# Užívateľ zadá číslo, následne, pomocou dvoch for cyklov, vypíšte každé číslo od 1 po zadané číslo
# do riadku toľko krát, aká je jeho hodnota
# Príklad:
# n = 2
# 1
# 2 2
# n = 4
# 1
# 2 2
# 3 3 3
# 4 4 4 4
def zvacsujuci_vystup():
    cislo = int(input('Zadaj cislo: '))
    for i in range(1, cislo + 1):
        for j in range(i):
            print(i, end=' ')
        print()


def zvacsujuci_vystup():  # bez 2 for cyklov
    cislo = int(input('Zadaj cislo: '))
    for i in range(1, cislo + 1):
        print((str(i) + ' ') * i)
