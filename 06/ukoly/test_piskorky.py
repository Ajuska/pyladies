from piskvorky import vyhodnot, tah
from ai import tah_pocitace

def test_vyhodnot():
    herni_pole = '-'*20
    assert vyhodnot(herni_pole) == '-'
    assert vyhodnot('---ooo--------------') == 'o'


def test_tah():
    herni_pole = '-'*20
    cislo_policka = 5
    symbol = 'o'
    assert tah(herni_pole, cislo_policka, symbol) == '-----o--------------'
