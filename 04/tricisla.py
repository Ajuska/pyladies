soucet = 0

for x in range(3):
    cislo = int(input('Zadej cislo:'))
    soucet += cislo
print(soucet)
if soucet > 10:
    print('Soucet je vetsi jak 10')
else:
    print('Soucet je mensi jak 10')
