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