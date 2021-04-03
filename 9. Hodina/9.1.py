# 9.1 Príklad
# Napíšte program, ktorý si od užívateľa vypýta string, a následne vypíše jeho dĺžku
# a prvé a posledné písmeno (ak je dĺžka stringu aspoň 1).
slovo = input('Zadaj slovo: ')
print('Dlzka je:', len(slovo))
if len(slovo) != 0:  # to iste ako len(slovo) >= 1
    print('Prvy znak:', slovo[0])
    print('Posledny znak:', slovo[-1])  # to iste ako print('Posledny znak', slovo[len(slovo) - 1])