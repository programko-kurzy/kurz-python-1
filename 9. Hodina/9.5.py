# 9.5 Príklad
# Napíšte funkciu vymen(slovo, znak, n), ktorej pošleme string, znak a číslo a tá vymení znak na n-tej
# pozícii zadaným znakom. Keďže sa toto nedá spraviť priamo pomocou slovo[n] = znak,
# musíme vytvoriť substring po n-tý znak pripojiť k nemu znak a k nim pripojiť
# substring od znaku na pozícii (n+1) po koniec stringu.
def vymen(slovo, znak, n):
    if 0 <= n < len(slovo):
        return slovo[:n] + znak + slovo[n + 1:]
    return slovo