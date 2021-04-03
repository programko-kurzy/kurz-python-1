# Vyskúšajte - Funckie
# Vytvorte si funkciu s vlastným názvom
# a skúste ju zavolať na rôznych miestach vo svojom kóde
def foo():
    print('Zaciatok mojej funkcie')
    print('Koniec mojej funkcie')


print('Prve volanie funkcie foo: ')
foo()
print('Druhe volanie funkcie foo: ')
foo()


# Funkcií môžete vytvoriť ľubovoľne veľa, prípadne volať jednu funkciu v druhej:
def foo2():
    foo()
    print('Zaciatok mojej funkcie')
    print('Koniec mojej funkcie')

foo2()

# Vyskúšajte - Parametre funcii
# Táto funkcia potrebuje jeden parameter a následne ho vypíše
def vypis(retazec):
    print(retazec)


vypis('Vypis tento retazec')


# Táto funkcia potrebuje dva parametre a vypíše ich súčet, prípadne zreťazenie ak sú to stringy.
def scitaj(cislo1, cislo2):
    print(cislo1 + cislo2)


scitaj(5, 6)
scitaj('a', 'b')