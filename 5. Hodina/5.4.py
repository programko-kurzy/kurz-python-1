# 5.4 Úloha na precvičenie
# Napíšte funkciu stvorec(a), ktorá vypíše štvorec so znakov „#” a kde a je dĺžka strany tohoto štvorca.
# Ak zavoláme stvorec(4), python vykreslí:
# „####
# ####
# ####
# ####“
def stvorec(a):
    for i in range(a):
        for j in range(a):
            print('#', end='')
        print()


def stvorec_druhy_sposob(a):
    for i in range(a):
        print('#' * a)


stvorec(4)

# 5.4.1 Úloha na precvičenie
# Upravte funkciu z predošlej úlohy tak, aby sme jej vedeli zadať aj znak z ktorého sa kreslí.
# Ak zavoláme stvorec(3, “A”), python vykreslí:
# „AAA
# AAA
# AAA“
def stvorec2(cislo, znak):
    for i in range(cislo):
        print(znak * cislo)


stvorec2(3, 'A')