# 2.3 Príklad
# Vytvorte program, ktorý dostane od užívateľa slovo, uloží si ho do premennej a
# následne ho 10 krát vypíše do riadku a dá medzi každé slovo čiarku
# Treba použiť for cyklus a print so správne zadaným parametrom end
slovo = input('Zadaj slovo: ')
for i in range(9):
    print(slovo, end=', ')
print(slovo)