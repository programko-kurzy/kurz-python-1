# 3.3 Príklad
# Napíšte for cyklus, ktorý vypíše všetky nepárne čísla od 0 po 10 (veľmi podobne ako v predchádzajúcom príklade)
for i in range(1, 11, 2):
    print(i, end=' ')
print()

# 3.3.1 Bonusový príklad
# Vylepšite príklad 3.3 tak, aby užívateľ zadal aj číslo, pokiaľ má program čísla vypisovať. Teda ak užívateľ zadá 5,
# budú sa vypisovať nepárne čísla od 0 po 5
# Hint: ak z input() získame číslo, uloží sa nám do premennej ako string a teda ho potom neviem použit vo funkcii
# range(), vypíše nám to error. Aby sme daný string pretypovali na integer, musíme použiť funkciu int(), teda
# napríklad, ak máme premennú cislo = input(‘Zadaj číslo >> ”) napíšeme range(int(cislo)).
pokym = int(input('Zadaj pokial: '))
for i in range(1, pokym + 1, 2):
    print(i, end=' ')
print()