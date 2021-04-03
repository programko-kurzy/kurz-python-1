# 7.3 Príklad
# Napíšte funkciu deleno(retazec, cislo), ktorá „podelí reťazec“ daným číslom
# Príklad deleno (“auto”, 2):
# “au”
# Príklad deleno (“trojkolka”, 3):
# tro”
# (Pozor treba použiť celočíslené delenie cislo // cislo,
# ak by ste použili klasické / výsledkom by mohlo byť necelé číslo
# a program by nefungoval)
def deleno(retazec, cislo):
    return retazec[:len(retazec) // cislo]