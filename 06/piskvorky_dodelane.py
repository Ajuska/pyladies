from random import randrange

def vyhodnot(herni_pole):
    "Vratí jednoznakový řetězec podle stavu hry"
    if 'xxx' in herni_pole:
        return 'x'
    if 'ooo' in herni_pole:
        return 'o'
    if '-' not in herni_pole:
        return '!'

    return '-'

def tah(herni_pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    herni_pole = zamen(herni_pole, cislo_policka, symbol)
    return herni_pole
    #zacatek = retezec[:pozice] , konec = retezec[pozice + 1:], return zacatek+symbol+konec

def zamen(retezec, pozice, znak):
    """Zamění znak na dané pozici
    Vrátí řetězec, který má na dané pozici daný znak;
    jinak je stejný jako vstupní retezec
    """
    return retezec[:pozice] + znak + retezec[pozice + 1:]

def tah_hrace(herni_pole):
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
                return tah(herni_pole, pozice, 'o')

def tah_pocitace(herni_pole):
    "Vybere pozici a vrátí herní pole se zaznamenaným tahem"
    while True:
        pozice = randrange(len(herni_pole)) #20
        if herni_pole[pozice] == '-':
            return tah(herni_pole, pozice, 'x')

def piskvorky1d():
    "Hra piškvorky"
    herni_pole = '-' * 20
    while vyhodnot(herni_pole) == '-':
        print(herni_pole)
        herni_pole = tah_hrace(herni_pole)
        if vyhodnot(herni_pole) != '-':
            break
        print(herni_pole)
        herni_pole = tah_pocitace(herni_pole)

    print(herni_pole)
    if vyhodnot(herni_pole) == '!':
        print('Remíza!')
    else:
        print('Vyhrál {}'.format(vyhodnot(pole)))


piskvorky1d()
