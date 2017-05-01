zvirata_1 = ['pes', 'kocka', 'kralik', 'had']
zvirata_2 = ['krecek', 'pes', 'andulka', 'kocka', 'lvice']
# seznam_1 = ['had', 'pes', 'andulka', 'kocka', 'kralik']
# seznam_2 = ['krecek', 'pes', 'lvice']
zvirata_obe = []
zvirata_jen_1 = []
zvirata_jen_2 = []


def vypis_tri_seznamy(seznam_1, seznam_2):
    for zvire_1 in seznam_1:
        if zvire_1 in seznam_2:
            zvirata_obe.append(zvire_1)
        if zvire_1 not in seznam_2:
             zvirata_jen_1.append(zvire_1)


    for zvire_2 in seznam_2:
        if zvire_2 not in seznam_1:
            zvirata_jen_2.append(zvire_2)

    return zvirata_obe, zvirata_jen_1, zvirata_jen_2


    print('Zvirata v oubou seznamech:', zvirata_obe)
    print('Zvirata v prvnim seznamu:', zvirata_jen_1)
    print('Zvirata v druhem seznamu:', zvirata_jen_2)



# vypis_tri_seznamy(zvirata_1, zvirata_2)
# vypis_tri_seznamy(seznam_1, seznam_2)
