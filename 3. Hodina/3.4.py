# 3.4 Príklad
# Napíšte for cyklus, ktorý vynásobí všetky čísla od 1 po 10 a vypíše tento výsledok
# Hint: dávajte si pozor, treba správne upraviť range, ak necháme defaultne range(11), prvé číslo bude vždy nula a ak
# násobíme nulou, vyjde nám vždy na konci nula.
sucin = 1
for cislo in range(1, 11):
    sucin *= cislo  # to iste ako: sucin = sucin * cislo
print(sucin)