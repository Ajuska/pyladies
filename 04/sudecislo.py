from random import randrange

cislo = randrange(9999999)

print(cislo)
vysledek = cislo%2
print(vysledek)

if vysledek == 0:
    print('Juchu je to sude cislo')
else:
    print('Jejda, je to liche cislo')
