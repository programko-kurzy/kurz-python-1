# 5.3 Príklad
# Napíšte funkciu poradie(n) ktorej pošlete jeden parameter (integer). Táto funkcia potom vypíše
# všetky čísla od 1 po n ktoré jej bolo zadané.
def poradie(n):
    for i in range(1, n + 1):
        print(i, end=' ')


poradie(10)