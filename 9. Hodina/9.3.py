# 9.3 Príklad
# Napíšte funkciu vymaz(slovo, n), ktorej pošleme string a číslo a tá vráti/vypíše podreťazec od daného znaku.
def vymaz(slovo, n):
    return slovo[:n] + slovo[n + 1:]