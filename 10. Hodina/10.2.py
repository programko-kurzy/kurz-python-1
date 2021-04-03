# 10.2 Príklad
# Napíšte program, ktorý si od užívateľa pýta dokola slovo, až kým zadané slovo nie je „stop“.
# Hint: vypýtajte si slovo od užívateľa a uložte ho do premennej ešte pred začatím
# while cyklu, aby ste túto premennú vedeli použiť v podmienke cyklu
slovo = input('Zadaj slovo: ')
while slovo != 'stop':
    print('okej pokracujeme')
    slovo = input('Zadaj slovo: ')
print('Okej skoncili sme')

# 10.2.1 Príklad
# Vylepšite predošlý príklad tak že si program bude od užívateľa pýtať dve slová,
# až kým slová nebudú rovnaké.
slovo1 = input('Zadaj prve slovo: ')
slovo2 = input('Zadaj druhe slovo: ')
while slovo1 != slovo2:
    print('Slova nie su take iste, skus znova')
    slovo1 = input('Zadaj prve slovo: ')
    slovo2 = input('Zadaj druhe slovo: ')
print('Slova sa rovnaju')