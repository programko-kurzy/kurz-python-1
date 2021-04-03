# 2.2 Príklad
# Za pomoci for cyklu napíšte program ktorý do riadku vypíše prvých n čísel od jedna.
# Teda pre N = 10 vypíše:
# 1 2 3 4 5 6 7 8 9 10
# Je treba použiť, for cyklus, range a print, s tým že range treba upraviť, aby nezačínala od 0 ale od 1.
n = 10
for i in range(1, n + 1):
    print(i, end=' ')