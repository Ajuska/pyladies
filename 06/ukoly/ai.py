from random import randrange
from tahnuti import tah

def zamen_xo(retezec):
    vysledek = []
    for znak in retezec:
        if znak == 'o':
            vysledek.append('x')
        elif znak == 'x':
            vysledek.append('o')
        else:
            vysledek.append(znak)
    return ''.join(vysledek)

def tah_pocitace(pole, symbol):
    if symbol == 'x':
        return tah_pocitace_x(pole)
    else:
        return zamen_xo(tah_pocitace_x(zamen_xo(pole)))

def kdo_zacina(herni_pole, na_tahu):
    if herni_pole.count('o') > herni_pole.count('x'):
        vic = 'o'
    elif herni_pole.count('o') < herni_pole.count('x'):
        vic = 'x'
    else:
        vic = '-'
    if vic == 'o':
        return 'o'
    elif vic == '-':
        return 'x'


def tah_pocitace_x(herni_pole):
    "Vybere pozici a vrátí herní pole se zaznamenaným tahem"
    if kdo_zacina(herni_pole, 'x') == 'x':
        utocit = True
    else:
        utocit = False

    if 'x-x' in herni_pole:
        a = herni_pole.index('x-x') + 1
        return tah(herni_pole, a, 'x')
    if 'xx-' in herni_pole:
        a = herni_pole.index('xx-') + 2
        return tah(herni_pole, a, 'x')
    if '-xx' in herni_pole:
        a = herni_pole.index('-xx')
        return tah(herni_pole, a, 'x')
    if 'o-o' in herni_pole:
        a = herni_pole.index('o-o') + 1
        return tah(herni_pole, a, 'x')
    if utocit:
        if '-x--' in herni_pole:
            a = herni_pole.index('-x--') + 2
            return tah(herni_pole, a, 'x')
        if '--x-' in herni_pole:
            a = herni_pole.index('--x-') + 1
            return tah(herni_pole, a, 'x')
        if '-o-' in herni_pole:
            plusminus = randrange(0, 3, 2)
            a = herni_pole.index('-o-') + plusminus
            return tah(herni_pole, a, 'x')
        if 'oo-' in herni_pole:
            a = herni_pole.index('oo-') + 2
            return tah(herni_pole, a, 'x')
        if '-oo' in herni_pole:
            a = herni_pole.index('-oo')
            return tah(herni_pole, a, 'x')
    else:
        if '-o-' in herni_pole:
            plusminus = randrange(0, 3, 2)
            a = herni_pole.index('-o-') + plusminus
            return tah(herni_pole, a, 'x')
        if 'oo-' in herni_pole:
            a = herni_pole.index('oo-') + 2
            return tah(herni_pole, a, 'x')
        if '-oo' in herni_pole:
            a = herni_pole.index('-oo')
            return tah(herni_pole, a, 'x')
        if '-x--' in herni_pole:
            a = herni_pole.index('-x--') + 2
            return tah(herni_pole, a, 'x')
        if '--x-' in herni_pole:
            a = herni_pole.index('--x-') + 1
            return tah(herni_pole, a, 'x')

    if '--------------------' in herni_pole:
        plusminus = randrange(0, 21)
        a = herni_pole.index('--------------------') + plusminus
        return tah(herni_pole, a, 'x')
    if '-----' in herni_pole:
        a = herni_pole.index('-----') + 2
        return tah(herni_pole, a, 'x')
    if '---' in herni_pole:
        a = herni_pole.index('---') + 1
        return tah(herni_pole, a, 'x')
    if 'x-' in herni_pole:
        a = herni_pole.index('x-') + 1
        return tah(herni_pole, a, 'x')
    if '-x' in herni_pole:
        a = herni_pole.index('-x')
        return tah(herni_pole, a, 'x')
    if '-o' in herni_pole:
        a = herni_pole.index('-o')
        return tah(herni_pole, a, 'x')
    if 'o-' in herni_pole:
        a = herni_pole.index('o-') + 1
        return tah(herni_pole, a, 'x')
