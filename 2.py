# Vyskusajte - nepovinne parametre
print('Ahoj svet', end='!')
print('tieto', 'slová', 'sú', 'oddelené', 'pomlčkami', sep='-')
x = input('Zadaj x:')
print(x, 'je tvoje zadané číslo')

# Vyskusajte - for cyklus
for i in range(10):
    print(i, end=' ')
print()

# Vyskusajte - Range
for i in range(10):
    print(i, end=' ')
print()

for i in range(2, 5):
    print(i, end=' ')
print()

for i in range(2, 11, 1):
    print(i, end=' ')
print()

for i in range(4, 100, 2):
    print(i, end=' ')
print()

for i in range(10, 0, -1):
    print(i, end=' ')
print()

# 2.1 Príklad
# Vytvorte program, ktorý si vypýta od užívateľa jeho meno (s peknou správou aby vedel čo má zadať) a
# následne vypíše toto meno.
meno = input('Zadajte meno:')
print(meno)

# 2.2 Príklad
# Za pomoci for cyklu napíšte program ktorý do riadku vypíše prvých n čísel od jedna.
# Teda pre N = 10 vypíše:
# 1 2 3 4 5 6 7 8 9 10
# Je treba použiť, for cyklus, range a print, s tým že range treba upraviť, aby nezačínala od 0 ale od 1.
n = 10
for i in range(1, n + 1):
    print(i, end=' ')

# 2.3 Príklad
# Vytvorte program, ktorý dostane od užívateľa slovo, uloží si ho do premennej a
# následne ho 10 krát vypíše do riadku a dá medzi každé slovo čiarku
# Treba použiť for cyklus a print so správne zadaným parametrom end
slovo = input('Zadaj slovo: ')
for i in range(9):
    print(slovo, end=', ')
print(slovo)


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
