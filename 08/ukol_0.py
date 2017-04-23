domaci_zvirata = ['pes', 'kocka', 'kralik', 'had']

def vypis_kratka_zvirata(zvirata):
    for zvire in zvirata:
        if len(zvire) < 5:
            print(zvire)

vypis_kratka_zvirata(domaci_zvirata)
