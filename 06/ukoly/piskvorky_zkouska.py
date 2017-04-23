from random import randrange
from tahnuti import tah
from ai import tah_pocitace

def vyhodnot(herni_pole):
    "Vratí jednoznakový řetězec podle stavu hry"
    if 'xxx' in herni_pole:
        return 'x'
    if 'ooo' in herni_pole:
        return 'o'
    if '-' not in herni_pole:
        return '!'

    return '-'

def tah_hrace(herni_pole, symbol):
    while True:
        try:
            pozice = int(input('Na kterou pozici chceš hrát?'))
        except ValueError:
            print('To není číslo!')
        else:
            pozice = pozice - 1
            if pozice < 0 or pozice >= len(herni_pole):
                print('Tam hrát nejde, tam není pole!')
            elif herni_pole[pozice] != '-':
                print('Tam hrát nejde, pozice je obsazena.')
            else:
                return tah(herni_pole, pozice, symbol)

def piskvorky1d():
    "Hra piškvorky"
    herni_pole = '-' * 20
    while vyhodnot(herni_pole) == '-':
        print(herni_pole)
        herni_pole = tah_hrace(herni_pole, 'o')
        if vyhodnot(herni_pole) != '-':
            break
        print(herni_pole)
        herni_pole = tah_pocitace(herni_pole, 'x')
    print(herni_pole)
    if vyhodnot(herni_pole) == '!':
        print('Remíza!')
    else:
        print('Vyhrál {}'.format(vyhodnot(herni_pole)))

piskvorky1d()
