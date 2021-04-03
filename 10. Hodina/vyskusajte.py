# Vyskúšajte
#
# Vyskúšajte si nasledovný kus kódu a pohrajte sa s rôznymi podmienkami,
# nech vidíte ako asi while cyklus funguje.
x = 10
while x > 5:
    print('x je stale viac ako 5')
    x -= 1
# Dávajte si však pozor, pri while cykle hrozí že naša podmienka nikdy nebude False a teda
# by nastalo takzvané zacyklenie a kód by nikdy neskončil.
x = 10
while x < 100:
    print('x je stale menej ako sto')
    x -= 1
# Ak napríklad spustíme nasledujúci kód, program nám buď zamrzne, alebo bude
# donekonečna vypisovať to isté až kým ho „nasilu“ nezastavíme. (Pretože ak od 10
# postupne odrátavame vždy jedna, číslo bude vždy menšie ako sto)