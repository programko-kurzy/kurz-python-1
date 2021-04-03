# Vyskúšajte - bloky
#
# Odsadenie klávesou tab:
for i in range(10):
    print('Tento kód funguje')
# Odsadenie jednou medzerou:

# for i in range(10):
#  print('Tento kód nefunguje')
#     print('Tento kód nefunguje')

# Druhý príklad vám vyhodí error, pretože si interpreter nebude istý kam jednotlivé príkazy patria

# ----------------------------------------------------------------------------------------------------------------------

# Vyskúšajte - bloky 2
for i in range(10):
    print('Tento kód sa opakuje')
    print('Tento kód sa taktiež opakuje')
for i in range(10):
    print('Tento kód sa opakuje')
print('Tento kód sa už neopakuje')

# Vyskúšajte si napísať rôzne kódy odsadené tabom, aby ste sa zoznámili s tým, ako presne blokovanie
# funguje. Teoreticky môže byť v jednom for cykle koľko riadkov len chcete. Dôležité je,
# aby boli všetky správne odsadené.


# Vyskúšajte - VYUŽÍVANIE RIADIACEJ PREMENNEJ FOR CYKLU
# Suma prvých desať čísel:
suma = 0
for i in range(10):
    suma = suma + i
print(suma)
# Výpis párnych čísel od 0 po 10
for i in range(0, 11, 2):
    print(i)
# Poskúšajte rôzne variácie range a pripomeňte si ako funguje