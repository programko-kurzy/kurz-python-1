# Vyskúšajte - Podretazce
# Rôzne rezy na rôznych slovách
# a všimnite si, že aj ak je druhé číslo väčšie ako dĺžka reťazcu, funkcia nám vráti jednoducho celý reťazec
retazec = 'Ahoj, ako sa mas?'
print(retazec[0:1])
print(retazec[2:5])
print(retazec[0:100])

# Čo sa stane ak nezadáme oba parametre, alebo ani jeden?
retazec = 'Ahoj, ako sa mas?'
print(retazec[2:])
print(retazec[:5])
print(retazec[:])

# Vyskúšajte
# Rezy so zápornými indexami
retazec = 'Ahoj, ako sa mas?'
print(retazec[-1:])
print(retazec[-5:-1])
print(retazec[:-5])


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


# 7.4 Úloha na precvičenie
# Napíšte funkciu search(word, sentence), ktorá funguje nasledovne:
# for cyklom prechádza premennú sentence robiac rezy od i do i + len(word).
# Ak sa tento rez rovná premennej word, vráti True, inak po skončení for cyklu False.
#
# Príklad search (“auto”, “auto”):
# vráti True
# Príklad search (“auto”, “atuo”):
# vráti False
# (Pozor treba použiť celočíslené delenie cislo // cislo,
# ak by ste použili klasické / výsledkom by mohlo byť necelé číslo
# a program by nefungoval)
def search(word, sentence):
    for i in range(len(sentence)):
        if sentence[i:i + len(word)] == word:
            return True
    return False



