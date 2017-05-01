barvy = {
    'hruska': 'zelena',
    'jablko': 'cervena',
    'meloun': 'zelena',
    'mrkev': 'oranzova',
}
print(barvy)

for ovoce, barva in barvy.items():
    print (ovoce, barva)

seznam_dvojic = [('Jmeno', 'Aja'), ('mesto', 'Brno')]
slovnik = dict(seznam_dvojic)
print(slovnik)

barvy_po_tydnu = dict(barvy) #vytvori novy slovnik
for klic, hodnota in barvy_po_tydnu.items():
    barvy_po_tydnu[klic] = 'cerno-hnedo-' + hodnota
print(barvy_po_tydnu)
print(barvy)
