# 2.4 Bonusový príklad
# Vylepšite príklad 2.1 tak, aby užívateľ zadal aj číslo, koľko krát sa má dané slovo vypísať a následne ho for cyklom
# toľko krát vypíšete.
# Hint: ak z input() získame číslo, uloží sa nám do premennej ako string a teda ho potom neviem použit vo funkcii
# range(), vypíše nám to error. Aby sme daný string pretypovali na integer, musíme použiť funkciu int(), teda
# napríklad, ak máme premennú cislo napíšeme range(int(cislo)).
cislo = int(input('Zadaj cislo: '))
slovo = input('Zadaj slovo: ')
for i in range(cislo - 1):
    print(slovo, end=', ')
print(slovo)