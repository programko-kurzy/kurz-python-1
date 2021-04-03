# Vyskúšajte
# Vrátenú hodnotu si vieme potom uložiť do premennej a využiť ju neskôr v kóde
def obvod_stvorca(a):
    return a * 4


a = 4
o = obvod_stvorca(a)
print('Stvorec s dlzkou', a, 'ma obvod', o)


# return môžeme použiť aj viacej krát, avšak akonáhle program na jeden narazí, funkcia vráti danú hodnotu
# a skončí, takže sa vždy vykoná iba jeden, a to prvý na ktorý program príde.
def je_parne(cislo):
    if cislo % 2 == 0:
        return str(cislo) + ' je parne'
    return str(cislo) + ' nie je parne'


for i in range(100):
    print(je_parne(i))


# Vyskúšajte - PRÁCA S REŤAZCAMI
# Spájať stringy sme si už vyskúšali vyššie, čo sa ale stane ak ich vynásobíme?
print('hello ' * 6)


# Vyskúšajte
# Vyskúšajte si vypísať reťazec po znakoch pomocou for cyklu a len().
veta = 'Ahoj, moj den je super, ucim sa totiz python'
for i in range(len(veta)):
    print(veta[i])
