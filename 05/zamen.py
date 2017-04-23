def zamen(retezec, pozice, znak):
    """Zamění znak na dané pozici
    Vrátí řetězec, který má na dané pozici daný znak;
    jinak je stejný jako vstupní retezec
    """

    return retezec[:pozice] + znak + retezec[pozice + 1:]

print(zamen('ahoj', 1, 'j'))
