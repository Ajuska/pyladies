zvirata = ['kocka', 'andulka', 'had', 'pes', 'kralik']
seznam_dvojic = []
seznam_abeceda = []

for hodnota in zvirata:
    klic = hodnota[1:]
    seznam_dvojic.append((klic, hodnota))
    seznam_dvojic.sort()

for klic, hodnota in seznam_dvojic:
    seznam_abeceda.append(hodnota)

print(seznam_abeceda)
