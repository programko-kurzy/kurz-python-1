# Vyskúšajte - bloky
#
# Odsadenie klávesou tab:
for i in range(10):
    print('Tento kód funguje')
# Odsadenie jednou medzerou:

# for i in range(10):
#  print('Tento kód nefunguje')
#     print('Tento kód nefunguje')

# Druhý príklad vám vyhodí error, pretože si interpreter nebude istý kam jednotlivé príkazy patria

# ----------------------------------------------------------------------------------------------------------------------

# Vyskúšajte - bloky 2
for i in range(10):
    print('Tento kód sa opakuje')
    print('Tento kód sa taktiež opakuje')
for i in range(10):
    print('Tento kód sa opakuje')
print('Tento kód sa už neopakuje')

# Vyskúšajte si napísať rôzne kódy odsadené tabom, aby ste sa zoznámili s tým, ako presne blokovanie
# funguje. Teoreticky môže byť v jednom for cykle koľko riadkov len chcete. Dôležité je,
# aby boli všetky správne odsadené.


# 3.1 Príklad
# Napíšte program, ktorý si vypýta od užívateľa dve slová (musíte dvakrát použiť príkaz input) a vypíše ich 5 krát,
# potom vypíše reťazec „medzera medzi for cyklami“ a následne zadané slová vypíše ešte 5 krát. T.j. musíte použiť
# dva for cykly.
slovo1 = input('Zadaj prve slovo: ')
slovo2 = input('Zadaj druhe slovo: ')
for i in range(5):
    print(slovo1)
    print(slovo2)
print('medzera medzi for cyklami')
for i in range(5):
    print(slovo1)
    print(slovo2)


# 3.2 Príklad
# Napíšte for cyklus, ktorý si v každej iterácii vypýta od užívateľa slovo a následne ho vypíše. For cyklus môže bežať
# ľubovoľne veľa krát.
n = 10
for i in range(n):
    slovo = input('Zadaj slovo: ')
    print('toto bolo tvoje slovo:', slovo)


# Vyskúšajte - VYUŽÍVANIE RIADIACEJ PREMENNEJ FOR CYKLU
# Suma prvých desať čísel:
suma = 0
for i in range(10):
    suma = suma + i
print(suma)
# Výpis párnych čísel od 0 po 10
for i in range(0, 11, 2):
    print(i)
# Poskúšajte rôzne variácie range a pripomeňte si ako funguje

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

# 3.4 Príklad
# Napíšte for cyklus, ktorý vynásobí všetky čísla od 1 po 10 a vypíše tento výsledok
# Hint: dávajte si pozor, treba správne upraviť range, ak necháme defaultne range(11), prvé číslo bude vždy nula a ak
# násobíme nulou, vyjde nám vždy na konci nula.
sucin = 1
for cislo in range(1, 11):
    sucin *= cislo  # to iste ako: sucin = sucin * cislo
print(sucin)


