velikost = input('Zadej cislo:')

for y in range(int(velikost)):
    for x in range(int(velikost)):
        if y == 0 or y == int(velikost)-1 or x == 0 or x == int(velikost)-1:
            print('A', end=' ')
        else:
            print('  ', end='')
    print()
