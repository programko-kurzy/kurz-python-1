# 6.4 Príklad
# Vytvorte funkciu obsahuje_znak(slovo, znak), ktorá prejde zadané slovo for cyklom, a ak narazí
# na zadaný znak, vráti true, inak po skončení for cyklu vráti false.
def obsahuje_znak(slovo, znak):
    for i in range(len(slovo)):
        if znak == slovo[i]:
            return True
    return False


def obsahuje_znak_inak(slovo, znak):
    for znak_v_slove in slovo:
        if znak == znak_v_slove:
            return True
    return False