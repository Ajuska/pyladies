print('Slyšela jsem tuto básničku:')
print()
soubor = open('rozsypanycaj.txt', encoding='utf-8')
for radek in soubor:
    print('    ' + radek)
soubor.close()
print()
print('Jak se ti líbí?')
