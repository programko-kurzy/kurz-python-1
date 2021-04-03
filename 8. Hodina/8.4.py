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