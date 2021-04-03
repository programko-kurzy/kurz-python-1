# Vyskúšajte
# Vrátenú hodnotu si vieme potom uložiť do premennej a využiť ju neskôr v kóde
def obvod_stvorca(a):
    return a * 4


a = 4
o = obvod_stvorca(a)
print('Stvorec s dlzkou', a, 'ma obvod', o)


# return môžeme použiť aj viacej krát, avšak akonáhle program na jeden narazí, funkcia vráti danú hodnotu
# a skončí, takže sa vždy vykoná iba jeden, a to prvý na ktorý program príde.
def je_parne(cislo):
    if cislo % 2 == 0:
        return str(cislo) + ' je parne'
    return str(cislo) + ' nie je parne'


for i in range(100):
    print(je_parne(i))


# 6.1 Príklad
# Vytvorte funkciu vylepsi(slovo), ktorej užívateľ pošle slovo, tá k nemu pripojí reťazec „je super“
# a vráti naspäť nový reťazec.
# (Stringy vieme sčítavať rovnako ako čísla, teda napríklad „toto a “ + „este toto“ nám vráti
# „toto a este toto“)
def vylepsi(slovo):
    return slovo + ' je super'


print(vylepsi('typek'))


# 6.2 Príklad
# Vytvorte dve funkcie:
# 1. je_pravouhly(alfa, beta, gamma) prijíma uhly trojuholníka, ak ich súčet nemôže byť trojuholník (nie je
# 180), vráti false, ak áno, tak vráti true ak trojuholník je pravouhlý a false ak nie je.
# 2. obsah_trojuholnika(a, b, alfa, beta, gamma): potrebuje dve odvesny trojuholníka a jeho uhly.
# Následne za pomoci funkcie 1. zistí či je pravouhlý, ak nie je vráti 0 a ak je vyráta jeho obsah z a a b
# a vráti ho.
def je_pravouhly(alfa, beta, gamma):
    if alfa + beta + gamma != 180:
        return False
    if alfa == 90 or beta == 90 or gamma == 90:
        return True
    return False


def je_pravouhly_lepsie(alfa, beta, gamma):
    if alfa + beta + gamma != 180:
        return False
    return alfa == 90 or beta == 90 or gamma == 90


def obsah_trojuholnika(a, b, alfa, beta, gamma):
    if je_pravouhly(alfa, beta, gamma):
        return 0
    return (a ** 2 + b ** 2) ** (1 / 2)


# Vyskúšajte - PRÁCA S REŤAZCAMI
# Spájať stringy sme si už vyskúšali vyššie, čo sa ale stane ak ich vynásobíme?
print('hello ' * 6)


# Vyskúšajte
# Vyskúšajte si vypísať reťazec po znakoch pomocou for cyklu a len().
veta = 'Ahoj, moj den je super, ucim sa totiz python'
for i in range(len(veta)):
    print(veta[i])


# 6.3 Príklad
# Vytvorte funkciu znak(slovo, pozicia), ktorej užívateľ pošle slovo a pozicia, z ktorej chce znak vypísať.
# Funkcia následne znak na tejto pozícii vráti, alebo vráti chybovú hlášku podľa vašej fantázie,
# ak táto pozícia v stringu neexistuje.
def znak(slovo, pozicia):
    if pozicia < 0 or pozicia > len(slovo):
        return "Chyba"
    return slovo[pozicia]


# 6.4 Príklad
# Vytvorte funkciu obsahuje_znak(slovo, znak), ktorá prejde zadané slovo for cyklom, a ak narazí
# na zadaný znak, vráti true, inak po skončení for cyklu vráti false.
def obsahuje_znak(slovo, znak):
    for i in range(len(slovo)):
        if znak == slovo[i]:
            return True
    return False


def obsahuje_znak_inak(slovo, znak):
    for znak_v_slove in slovo:
        if znak == znak_v_slove:
            return True
    return False


# 6.5 Úloha na precvičenie
# Napíšte funkciu badge(name), ktorá zistí dĺžku mena a podľa nej vypíše zadané meno s rámčekom.
#
# Príklad badge(“Ema”):
# *******
# *     *
# * Ema *
# *     *
# *******
def badge(name):
    print('*' * (len(name) + 4))
    print('*' + ' ' * (len(name) + 2) + '*')
    print('*' + ' ' + name + ' ' + '*')
    print('*' + ' ' * (len(name) + 2) + '*')
    print('*' * (len(name) + 4))


badge('Ema')
