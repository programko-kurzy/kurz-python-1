# 7.2 Príklad
# Vytvorte program, ktorému užívateľ zadá reťazec a program ho vypíše postupne, najprv prvý znak, potom prvé
# dva, a tak ďalej až kým nevypíše celý reťazec
# Napríklad užívateľ zadá: „Ahoj“
# Program vypíše:
# „A“
# „Ah“
# „Aho“
# „Ahoj“
def postupne_vypisovanie():
    slovo = input('zadaj slovo')
    for i in range(1, len(slovo) + 1):
        print(slovo[:i])