from random import randrange

def hod():
    pocet_hodu = 0
    while True:
        hod = randrange(1, 7)
        pocet_hodu = pocet_hodu+1
        print(pocet_hodu, hod)
        if hod == 6:
            break
    return pocet_hodu

prvni_pocet = hod()
vitez_pocet_hodu = prvni_pocet
vitez = 'prvni hráč'

druhy_pocet = hod()
if vitez_pocet_hodu < druhy_pocet:
    vitez_pocet_hodu = druhy_pocet
    vitez = 'druhy hráč'

treti_pocet = hod()
if vitez_pocet_hodu < treti_pocet:
    vitez_pocet_hodu = treti_pocet
    vitez = 'třetí hráč'

ctvrty_pocet = hod()
if vitez_pocet_hodu < ctvrty_pocet:
    vitez_pocet_hodu = ctvrty_pocet
    vitez = 'čtvrtý hráč'

print(vitez)
