# 6.3 Príklad
# Vytvorte funkciu znak(slovo, pozicia), ktorej užívateľ pošle slovo a pozicia, z ktorej chce znak vypísať.
# Funkcia následne znak na tejto pozícii vráti, alebo vráti chybovú hlášku podľa vašej fantázie,
# ak táto pozícia v stringu neexistuje.
def znak(slovo, pozicia):
    if pozicia < 0 or pozicia > len(slovo):
        return "Chyba"
    return slovo[pozicia]