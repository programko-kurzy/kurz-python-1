# 9.2 Príklad
# Napíšte program, ktorý si od užívateľa vypýta string, a ak má string aspoň 1 znak, vypíše ho bez
# prvého znaku. Teda, pre vstup „Slovo“, vypíše „lovo“.
slovo = input('Zadaj slovo: ')
if len(slovo) != 0:
    print(slovo[1:])