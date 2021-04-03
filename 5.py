# Vyskúšajte - Funckie
# Vytvorte si funkciu s vlastným názvom
# a skúste ju zavolať na rôznych miestach vo svojom kóde
def foo():
    print('Zaciatok mojej funkcie')
    print('Koniec mojej funkcie')


print('Prve volanie funkcie foo: ')
foo()
print('Druhe volanie funkcie foo: ')
foo()


# Funkcií môžete vytvoriť ľubovoľne veľa, prípadne volať jednu funkciu v druhej:
def foo():
    print('Zaciatok mojej funkcie')
    print('Koniec mojej funkcie')


def foo2():
    foo()
    print('Zaciatok mojej funkcie')
    print('Koniec mojej funkcie')


foo2()


# Vyskúšajte - Parametre funcii
# Táto funkcia potrebuje jeden parameter a následne ho vypíše
def vypis(retazec):
    print(retazec)


vypis('Vypis tento retazec')


# Táto funkcia potrebuje dva parametre a vypíše ich súčet, prípadne zreťazenie ak sú to stringy.
def scitaj(cislo1, cislo2):
    print(cislo1 + cislo2)


scitaj(5, 6)
scitaj('a', 'b')


# 5.1 Príklad
#
# Napíšte funkciu pozdrav(meno) ktorej pošlete jeden parameter, meno, a ona ho pozdraví.
# Teda ak zavoláme funkciu pozdrav(“Matej”), program vypíše napríklad „Ahoj, Matej“
def pozdrav(meno):
    print('Ahoj,', meno)


pozdrav('Matej')


# 5.2 Príklad
# Napíšte funkciu opakuj(slovo, pocet) ktorej pošlete dva parametre, nejaké slovo a koľko krát sa má vypísať
# (Teda string a integer).
# Teda ak zavoláme funkciu opakuj(“woop”, 3), program vypíše:
# „woop
# woop
# woop“
def opakuj(slovo, pocet):
    for i in range(pocet):
        print(slovo)


opakuj('woop', 3)


# 5.3 Príklad
# Napíšte funkciu poradie(n) ktorej pošlete jeden parameter (integer). Táto funkcia potom vypíše
# všetky čísla od 1 po n ktoré jej bolo zadané.
def poradie(n):
    for i in range(1, n + 1):
        print(i, end=' ')


poradie(10)


# 5.4 Úloha na precvičenie
# Napíšte funkciu stvorec(a), ktorá vypíše štvorec so znakov „#” a kde a je dĺžka strany tohoto štvorca.
# Ak zavoláme stvorec(4), python vykreslí:
# „####
# ####
# ####
# ####“
def stvorec(a):
    for i in range(a):
        for j in range(a):
            print('#', end='')
        print()


def stvorec_druhy_sposob(a):
    for i in range(a):
        print('#' * a)


stvorec(4)


# 5.4.1 Úloha na precvičenie
# Upravte funkciu z predošlej úlohy tak, aby sme jej vedeli zadať aj znak z ktorého sa kreslí.
# Ak zavoláme stvorec(3, “A”), python vykreslí:
# „AAA
# AAA
# AAA“
def stvorec(cislo, znak):
    for i in range(cislo):
        print(znak * cislo)


stvorec(3, 'A')

