osoby = 'mama', 'teta', 'babicka'

print(osoby)

for osoba in osoby:
    print(osoba)


seznam = []
seznam.append((1,2,3))
print(seznam)

def podil_a_zbytek(a, b):
    return a//b, a%b

podil, zbytek = podil_a_zbytek(10, 3)
print(podil, zbytek)


osoby = ['mama', 'teta', 'vrah']
vlastnosti = ['hodna', 'mila', 'zakerny']
for osoba, vlastnost in zip(osoby, vlastnosti):
    print(vlastnost, osoba)
print(list(zip(osoby, vlastnosti)))

for n, osoba in enumerate(osoby):
    print(n,osoba)
