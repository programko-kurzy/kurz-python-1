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