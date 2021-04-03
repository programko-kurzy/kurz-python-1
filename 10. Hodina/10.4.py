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