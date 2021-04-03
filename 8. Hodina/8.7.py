# 8.7 Príklad
# Užívateľ zadá slovo. Zistite či sú prvé a posledné písmeno rovnaké
# a vypíšte či áno alebo nie.
slovo = input('Zadaj slovo: ')
if len(slovo) == 0:
    print('Slovo je prazdne')
elif slovo[0] == slovo[-1]:  # to iste ako elif slovo[0] == slovo[len(slovo) - 1]
    print('Ano, prve a posledne pismeno su rovnake')
else:
    print('Nie, prve a posledne pismenu nie su rovnake')