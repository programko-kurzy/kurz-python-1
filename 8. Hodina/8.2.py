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