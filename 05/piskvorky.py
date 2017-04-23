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

def zamen(retezec, pozice, znak):
    """Zamění znak na dané pozici
    Vrátí řetězec, který má na dané pozici daný znak;
    jinak je stejný jako vstupní retezec
    """
    return retezec[:pozice] + znak + retezec[pozice + 1:]

def tah_hrace(herni_pole):
    while True:
        pozice = int(input('Na kterou pozici chceš hrát?'))
        if pozice < 0 or pozice > 19:
            print('Zadej cislo od 0-19.')
        elif herni_pole[pozice] != '-':
            print('Pozice obsazena.')
                    else:
            break

    herni_pole = tah(herni_pole, pozice, 'x')
    return herni_pole


print(vyhodnot('oo-o--x'))
print(vyhodnot('ooo-o--x'))
print(vyhodnot('oo-o--xxx'))
print(vyhodnot('ooxoxoxx'))


print(tah('--------------------', 5, 'x'))
print(tah('--------------------', 2, 'x'))
print(tah('--------------------', 3, 'x'))
print(tah('--------------------', 4, 'x'))

print(tah_hrace('x-------------'))
