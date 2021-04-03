# 9.4 Príklad
# Napíšte funkciu obsahuje(slovo, znak), ktorej pošlete string a string dĺžky jedna (písmeno)
# a ona vráti true alebo false podľa toho či sa znak nachádza v premennej slovo.
def obsahuje_1(slovo, znak):
    for i in range(len(slovo)):
        if znak == slovo[i]:
            return True
    return False


def obsahuje_1_2(slovo, znak):
    for znak_v_slove in slovo:
        if znak_v_slove == znak:
            return True
    return False


def obsahuje_1_3(slovo, znak):
    return znak in slovo

# 9.4.1 Príklad
# Vylepšite funkciu obsahuje(..) tak aby nevracala true alebo false, ale naopak vrátila
# index, na ktorom sa písmeno nachádza, alebo -1 ak sa v stringu nenachádza
def obsahuje_2(slovo, znak):
    for i in range(len(slovo)):
        if znak == slovo[i]:
            return i
    return -1


def obsahuje_2_2(slovo, znak):
    return slovo.index(znak)