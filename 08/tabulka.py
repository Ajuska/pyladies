from pprint import pprint

#seznam s deseti prvky

nasobilka = []

for a in range(10):
    radek = [] #vytvoreni maleho seznamu
    for b in range(10):
        prvek = a* b
        radek.append(prvek)
    nasobilka.append(radek) #pockracuje v tvoreni nasobilky


pprint(nasobilka)
print(nasobilka[5][3])

nasobilka[3][5] = 8 #prepise misto v radku z 15 na 8

for radek in nasobilka:
    for cislo in radek:
        print(cislo, end=' ')
    print()
