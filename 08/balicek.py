from random import choice, shuffle

hodnoty = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']
barvy = ['Srdce', 'Piky', 'Kary', 'Krize']

balicek_karet = []

for hodnota in hodnoty:
    for barva in barvy:
        prvek = '{} {}'.format(hodnota, barva)
        balicek_karet.append(prvek)


print(choice(balicek_karet))
print(choice(["kamen, nuzky"]))
shuffle(balicek_karet)
print(balicek_karet)
