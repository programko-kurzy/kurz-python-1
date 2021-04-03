# 6.5 Úloha na precvičenie
# Napíšte funkciu badge(name), ktorá zistí dĺžku mena a podľa nej vypíše zadané meno s rámčekom.
#
# Príklad badge(“Ema”):
# *******
# *     *
# * Ema *
# *     *
# *******
def badge(name):
    print('*' * (len(name) + 4))
    print('*' + ' ' * (len(name) + 2) + '*')
    print('*' + ' ' + name + ' ' + '*')
    print('*' + ' ' * (len(name) + 2) + '*')
    print('*' * (len(name) + 4))


badge('Ema')