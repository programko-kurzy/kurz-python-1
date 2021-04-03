# Vyskúšajte - Podretazce
# Rôzne rezy na rôznych slovách
# a všimnite si, že aj ak je druhé číslo väčšie ako dĺžka reťazcu, funkcia nám vráti jednoducho celý reťazec
retazec = 'Ahoj, ako sa mas?'
print(retazec[0:1])
print(retazec[2:5])
print(retazec[0:100])

# Čo sa stane ak nezadáme oba parametre, alebo ani jeden?
retazec = 'Ahoj, ako sa mas?'
print(retazec[2:])
print(retazec[:5])
print(retazec[:])

# Vyskúšajte
# Rezy so zápornými indexami
retazec = 'Ahoj, ako sa mas?'
print(retazec[-1:])
print(retazec[-5:-1])
print(retazec[:-5])