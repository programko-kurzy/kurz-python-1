# Vyskúšajte
#
# Vyskúšajte si nasledovný kus kódu a pohrajte sa s rôznymi podmienkami,
# nech vidíte ako asi while cyklus funguje.
x = 10
while x > 5:
    print('x je stale viac ako 5')
    x -= 1
# Dávajte si však pozor, pri while cykle hrozí že naša podmienka nikdy nebude False a teda
# by nastalo takzvané zacyklenie a kód by nikdy neskončil.
x = 10
while x < 100:
    print('x je stale menej ako sto')
    x -= 1
# Ak napríklad spustíme nasledujúci kód, program nám buď zamrzne, alebo bude
# donekonečna vypisovať to isté až kým ho „nasilu“ nezastavíme. (Pretože ak od 10
# postupne odrátavame vždy jedna, číslo bude vždy menšie ako sto)


# 10.1 Príklad
# Napíšte program, ktorý pomocou while cyklu vypíše 10 krát ľubovoľné slovo.
# Skúste vymyslieť aspoň dve rôzne podmienky, ako by ste to vedeli dosiahnuť.
x = 0
while x != 10: # x < 10, x <= 9
    print(x, end=' ')
    x += 1


# 10.2 Príklad
# Napíšte program, ktorý si od užívateľa pýta dokola slovo, až kým zadané slovo nie je „stop“.
# Hint: vypýtajte si slovo od užívateľa a uložte ho do premennej ešte pred začatím
# while cyklu, aby ste túto premennú vedeli použiť v podmienke cyklu
slovo = input('Zadaj slovo: ')
while slovo != 'stop':
    print('okej pokracujeme')
    slovo = input('Zadaj slovo: ')
print('Okej skoncili sme')


# 10.2.1 Príklad
# Vylepšite predošlý príklad tak že si program bude od užívateľa pýtať dve slová,
# až kým slová nebudú rovnaké.
slovo1 = input('Zadaj prve slovo: ')
slovo2 = input('Zadaj druhe slovo: ')
while slovo1 != slovo2:
    print('Slova nie su take iste, skus znova')
    slovo1 = input('Zadaj prve slovo: ')
    slovo2 = input('Zadaj druhe slovo: ')
print('Slova sa rovnaju')


# 10.3 Príklad
# Napíšte program, ktorý si od užívateľa vypýta číslo, ktoré následne vo while cykle
# delíte 10, kým je číslo väčšie ako 0.
# Čo týmto spôsobom počítame?
cislo = int(input('Zadaj cislo: '))
vysledok = 0
while cislo > 0:
    cislo //= 10
    vysledok += 1
# Pocet cifier


# 10.4 Príklad
# Napíšte program, ktorý si od užívateľa pýta dve čísla, až kým prvé číslo nie je väčšie ako druhé.
cislo1 = int(input('Zadaj prve cislo: '))
cislo2 = int(input('Zadaj druhe cislo: '))
while cislo1 <= cislo2:
    print('Prve cislo nie je vacsie ako druhe')
    cislo1 = int(input('Zadaj prve cislo: '))
    cislo2 = int(input('Zadaj druhe cislo: '))
print('Prve cislo je vacsie ako druhe')


# 10.4.1 Bonusový príklad
# Vylepšite príklad 10.4 tak, že keď získame dve čísla kde prvé je väčšie, vypíšte pomocou
# while cyklu „Prvé číslo je stále väčšie!“ toľko krát o koľko je prvé číslo väčšie.
cislo1 = int(input('Zadaj prve cislo: '))
cislo2 = int(input('Zadaj druhe cislo: '))
while cislo1 > cislo2:
    print('Prvé číslo je stále väčšie!')
    cislo1 -= 1
