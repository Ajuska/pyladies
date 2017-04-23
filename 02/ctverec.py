# Geometricka kalkulacka
strana = int(input('Jaka je strana ctverce?'))

dava_smysl = (strana > 0)

if dava_smysl:
    print('obvod ctverce se stranou', strana, 'je', strana*4, 'cm')
    print('obsah cterce se stranou', strana, 'je', strana**2, 'cm2')
elif strana == 0:
    print('Prazdny ctverec je prazdny')
else:
    print('To nedava smysl')

jmeno = input('Jak se jmenujes?')
print('Jsi sikovna', jmeno, '!')
