# 9.1 Príklad
# Napíšte program, ktorý si od užívateľa vypýta string, a následne vypíše jeho dĺžku
# a prvé a posledné písmeno (ak je dĺžka stringu aspoň 1).
slovo = input('Zadaj slovo: ')
print('Dlzka je:', len(slovo))
if len(slovo) != 0:  # to iste ako len(slovo) >= 1
    print('Prvy znak:', slovo[0])
    print('Posledny znak:', slovo[-1])  # to iste ako print('Posledny znak', slovo[len(slovo) - 1])


# 9.2 Príklad
# Napíšte program, ktorý si od užívateľa vypýta string, a ak má string aspoň 1 znak, vypíše ho bez
# prvého znaku. Teda, pre vstup „Slovo“, vypíše „lovo“.
slovo = input('Zadaj slovo: ')
if len(slovo) != 0:
    print(slovo[1:])


# 9.3 Príklad
# Napíšte funkciu vymaz(slovo, n), ktorej pošleme string a číslo a tá vráti/vypíše podreťazec od daného znaku.
def vymaz(slovo, n):
    return slovo[:n] + slovo[n + 1:]


# 9.4 Príklad
# Napíšte funkciu obsahuje(slovo, znak), ktorej pošlete string a string dĺžky jedna (písmeno)
# a ona vráti true alebo false podľa toho či sa znak nachádza v premennej slovo.
def obsahuje(slovo, znak):
    for i in range(len(slovo)):
        if znak == slovo[i]:
            return True
    return False


def obsahuje(slovo, znak):
    for znak_v_slove in slovo:
        if znak_v_slove == znak:
            return True
    return False


def obsahuje(slovo, znak):
    return znak in slovo


# 9.4.1 Príklad
# Vylepšite funkciu obsahuje(..) tak aby nevracala true alebo false, ale naopak vrátila
# index, na ktorom sa písmeno nachádza, alebo -1 ak sa v stringu nenachádza
def obsahuje(slovo, znak):
    for i in range(len(slovo)):
        if znak == slovo[i]:
            return i
    return -1


def obsahuje(slovo, znak):
    return slovo.index(znak)


# 9.5 Príklad
# Napíšte funkciu vymen(slovo, znak, n), ktorej pošleme string, znak a číslo a tá vymení znak na n-tej
# pozícii zadaným znakom. Keďže sa toto nedá spraviť priamo pomocou slovo[n] = znak,
# musíme vytvoriť substring po n-tý znak pripojiť k nemu znak a k nim pripojiť
# substring od znaku na pozícii (n+1) po koniec stringu.
def vymen(slovo, znak, n):
    if 0 <= n < len(slovo):
        return slovo[:n] + znak + slovo[n + 1:]
    return slovo


# 9.6 Príklad
# Napíšte funkciu skopiruj(slovo), ktorá dostane string a vráti string rovnakej dĺžky,
# ale všetky písmená budú „_“.
# Napríklad, pre vstup: „ahoj“
# funkcia vráti: „____“
def skopiruj(slovo):
    return '_' * len(slovo)


# 9.7 Bonusový príklad - hra obesenec
# Najprv necháme užívateľa aby zadal slovo, ktoré sa bude snažiť „uhádnuť“
# Následne si pomocou funkcie skopiruj(slovo), vytvoríme kópiu s podtržítkami
# a uložíme ju do premennej.
#
# Ďalej napíšeme funkciu hadaj(slovo, kopia, znak), ktorá dostane string, jeho kópiu a znak.
# Vytvoríme si premennú najdene = False a string slovo prechádzame for cyklom.
# Ak narazíme na písmeno ktoré je rovnaké ako znak, zavoláme funkciu kopia = vymen(..)
# pre kopia, znak, aktuálny index a najdene nastavíme na True.
# Nakoniec, ak je najdene == True vypíšeme “Uhádol si!”,
# inak “Toto písmeno v slove nie je“ a vrátime novú kópiu slova.
slovo = input()


def hadaj(slovo, kopia, znak):
    najdene = False
    for i in range(len(slovo)):
        if slovo[i] == znak:
            kopia = vymen(kopia, znak, i)
            najdene = True
    if najdene:
        print('Uhadol si!')
    else:
        print('Toto písmeno v slove nie je')
    return kopia


# 9.7.1 priklad
#
# Aby sa hra dala aj hrať, musíme ešte dokončiť kolá a vstup písmen od užívateľa.
# Pre jednoduchú verziu, môžeme dať užívateľovi toľko pokusov, ako je v zadanom slove písmen.
# To znamená že po zadaní slova na uhádnutie a vytvorení jeho kópie zistíme jeho dĺžku
# a použijeme for cyklus v ktorom bude užívateľ hádať. V každom cykle teda užívateľ
# zadá písmeno (ak zadá reťazec dlhší ako jedno písmeno, stratí jeden pokus) a následne zavoláme funkciu
#
# hadaj(slovo, kopia, znak) a uložíme jej výsledok znova do premennej kopia.
# Ak sa kópia po skončení for cyklu rovná prvotne zadanému slovu, užívateľ vyhral, inak prehral.
slovo = input()
kopia = skopiruj(slovo)
hotovo = False
for i in range(len(slovo)):
    if not hotovo:
        znak = input('Zadaj znak: ')
        kopia = hadaj(slovo, kopia, znak)
        if kopia == slovo:
            hotovo = True
if kopia == slovo:
    print('Vyhral si')