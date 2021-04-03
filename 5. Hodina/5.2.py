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