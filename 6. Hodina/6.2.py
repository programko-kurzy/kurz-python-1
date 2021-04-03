# 6.2 Príklad
# Vytvorte dve funkcie:
# 1. je_pravouhly(alfa, beta, gamma) prijíma uhly trojuholníka, ak ich súčet nemôže byť trojuholník (nie je
# 180), vráti false, ak áno, tak vráti true ak trojuholník je pravouhlý a false ak nie je.
# 2. obsah_trojuholnika(a, b, alfa, beta, gamma): potrebuje dve odvesny trojuholníka a jeho uhly.
# Následne za pomoci funkcie 1. zistí či je pravouhlý, ak nie je vráti 0 a ak je vyráta jeho obsah z a a b
# a vráti ho.
def je_pravouhly(alfa, beta, gamma):
    if alfa + beta + gamma != 180:
        return False
    if alfa == 90 or beta == 90 or gamma == 90:
        return True
    return False


def je_pravouhly_lepsie(alfa, beta, gamma):
    if alfa + beta + gamma != 180:
        return False
    return alfa == 90 or beta == 90 or gamma == 90


def obsah_trojuholnika(a, b, alfa, beta, gamma):
    if je_pravouhly(alfa, beta, gamma):
        return 0
    return (a ** 2 + b ** 2) ** (1 / 2)