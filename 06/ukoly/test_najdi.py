from najdi import najdi_symboly

def test_najdi():
    herni_pole = 20 * ('-')
    symbol_hrace = 'o'
    assert najdi_symboly(herni_pole, symbol_hrace) == list()
    assert najdi_symboly('--o-o-o-o', symbol_hrace) == [2, 4, 6, 8]
