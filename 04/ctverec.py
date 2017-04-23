for y in range(5):
    for x in range(6):
        if y == 0 or y == 4 or x == 0 or x == 5:
            print('A', end=' ')
        else:
            print('  ', end='')
    print()
