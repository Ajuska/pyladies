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
