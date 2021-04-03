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


def zvacsujuci_vystup_lepsie():  # bez 2 for cyklov
    cislo = int(input('Zadaj cislo: '))
    for i in range(1, cislo + 1):
        print((str(i) + ' ') * i)