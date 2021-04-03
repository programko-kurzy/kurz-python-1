# 4.3 Príklad
# Napíšte program, ktorý si od užívateľa vypýta dve čísla. Ak je súčin týchto čísel väčší ako 1000, vypíše „ok.“, inak
# vypíše „nabudúce prosím zadajte väčšie čísla“.
# Pripomienka: aby sme so zadanými číslami mohli robiť matematické operácie, musíme ich najprv zmeniť zo stringu
# na int a to príkazom int(), teda: x = int(input(„Vaša správa“))
cislo1 = int(input('Zadaj prve cislo'))
cislo2 = int(input('Zadaj druhe cislo'))
if cislo1 * cislo2 > 1000:
    print('ok')
else:
    print('nabudúce prosím zadajte väčšie čísla')