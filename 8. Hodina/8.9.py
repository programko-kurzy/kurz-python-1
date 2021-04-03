# 8.9 Príklad
# Vytvorte funkciu parnePismena, ktorá dostane jedno slovo, a vypíše iba
# písmená na párnych pozíciách
# Príklad: slovo = „Ahoj“
# Výpis: „Ao“ (pozície začínajú od nula)
def parne_pismena(slovo):
    for i in range(0, len(slovo), 2):
        print(slovo[i], end='')

def parne_pismena_lepsie(slovo):
    print(slovo[::2])