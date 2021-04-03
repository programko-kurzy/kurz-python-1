# 8.8 Príklad
# Vytvorte funkciu sucetAleboSucin, ktorá dostane dve čísla, tie vynásobí a ak je súčin menší ako 1000,
# vráti ho, inak vráti namiesto neho ich súčet
def sucetAleboSucin(cislo1, cislo2):
    sucin = cislo1 * cislo2
    if sucin < 1000:
        return sucin
    return cislo1 + cislo2