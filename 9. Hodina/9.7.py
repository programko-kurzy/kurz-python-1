# Potrebujeme funkcie z príkladov 9.6 a 9.5
def vymen(slovo, znak, n):
    if 0 <= n < len(slovo):
        return slovo[:n] + znak + slovo[n + 1:]
    return slovo

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