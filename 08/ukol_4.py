zvirata_1 = ['pes', 'kocka', 'kralik', 'had']
zvirata_2 = ['krecek', 'pes', 'andulka', 'kocka', 'lvice']
zvirata_obe = []
zvirata_jen_1 = []
zvirata_jen_2 = []


def vrat_tri_seznamy(seznam_1, seznam_2):
    for zvire in seznam_1:
        if zvire in seznam_2:
            return zvirata_obe.append(zvire)
            print(zvirata_obe)
        if zvire not in seznam_2:
            return zvirata_jen_1.append(zvire) and zvirata_jen_2.append(zvire)
            print(zvirata_jen_1)
            print(zvirata_jen_2)

vrat_tri_seznamy(zvirata_1, zvirata_2)
