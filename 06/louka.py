barva_travy = 'zelená'
pocet_kotatek = 28

def popis_stav():
    popis = ('Tráva je {barva} a prohání se po ní {pocet} koťátek')
    return popis.format(
                barva=barva_travy,
                pocet=pocet_kotatek)
