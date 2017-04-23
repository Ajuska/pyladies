vek = int(input('Kolik ti je let? '))
if vek >= 150:
    print('A ze kterépak jsi planety?')
elif vek >= 18:
    # Tahle větev se např. pro "200" už neprovede.
    print('Můžeme nabídnout: víno, cider, nebo vodku.')
elif vek >= 1:
    print('Můžeme nabídnout: mléko, čaj, nebo vodu')
elif vek >= 0:
    print('Sunar už bohužel došel.')
else:
    # Nenastala ani nedna ze situací výše – muselo to být záporné
    print('Návštěvníky z budoucnosti tady nevidíme rádi.')
