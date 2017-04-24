domaci_zvirata = ['pes', 'kocka', 'kralik', 'had']

def vypis_kratka_zvirata(zvirata):
    for zvire in zvirata:
        if len(zvire) < 5:
            print(zvire)


def vypis_k_zvirata(zvirata):
    for zvire in zvirata:
        if zvire[0] == 'k':
            print(zvire)


def overit_seznam_zvirat(zvirata):
    if zvirata in domaci_zvirata:
        print('Ano')
        return True
    else:
        print('Ne')
        return False


vypis_kratka_zvirata(domaci_zvirata)
vypis_k_zvirata(domaci_zvirata)

otazka_pro_overeni = input('Zadej jemno zvirete pro overeni v seznamu:')
overit_seznam_zvirat(otazka_pro_overeni)
