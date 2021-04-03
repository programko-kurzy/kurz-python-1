# 7.1 Príklad
# Vytvorte program, ktorému užívateľ zadá reťazec a program vypíše jeho prvé štyri znaky.
def prve_4_znaky():
    slovo = input('zadaj slovo')
    print(slovo[:4])


# 7.1.1 Príklad
# Vylepšite predošlý program:
# Pomocou funkcie len() z predošlej hodiny sa najprv spýtajte či je zadané slovo dostatočne dlhé, a ak je kratšie
# ako 4 znaky, vypíšte ľubovoľnú chybovú hlášku
def prve_4_znaky_lepsie():
    slovo = input('zadaj slovo')
    if len(slovo) < 4:
        print('Neni dost dlhe')
    else:
        print(slovo[:4])


# 7.1.2 Príklad
# Vylepšite predošlý program ešte raz:
# Nechajte užívateľa zadať aj počet znakov ktoré sa majú vypísať, takže ak užívateľ zadá napríklad:
# „Nejaké slovo“
# „4“
# Program vypíše: „Neja“
# (Aby ste mohli použiť zadané číslo v reze, musíte ho prekonvertovať na integer funkciou int())
def prvych_n_znaky():
    cislo = int(input('zadaj cislo'))
    slovo = input('zadaj slovo')
    if len(slovo) < cislo:
        print('Neni dost dlhe')
    else:
        print(slovo[:cislo])