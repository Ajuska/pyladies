print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano':
    stastna = True
elif stastna_retezec == 'ne':
    stastna = False
else:
    print('Nerozumím!')

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    bohata = True
elif bohata_retezec == 'ne':
    bohata = False
else:
    print('Nerozumím!')


if stastna:
    if bohata:
        print('Gratuluji!')
    else:
        print('Zkus míň utrácet.')
else:
    if bohata:
        print('Zkus se víc usmívat.')
    else:
        print('To je mi líto.')
