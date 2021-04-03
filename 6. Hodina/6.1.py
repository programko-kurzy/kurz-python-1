# 6.1 Príklad
# Vytvorte funkciu vylepsi(slovo), ktorej užívateľ pošle slovo, tá k nemu pripojí reťazec „je super“
# a vráti naspäť nový reťazec.
# (Stringy vieme sčítavať rovnako ako čísla, teda napríklad „toto a “ + „este toto“ nám vráti
# „toto a este toto“)
def vylepsi(slovo):
    return slovo + ' je super'


print(vylepsi('typek'))