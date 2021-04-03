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