stastna_a_bohata = input('Jsi šťastná, bohatá, oboje nebo ani jedno?')

if stastna_a_bohata:
    if stastna_a_bohata == 'oboje':
        print('Gratuluji!')
    elif stastna_a_bohata == 'bohatá':
        print('Zkus se víc usmívat.')
    elif stastna_a_bohata == 'šťastná':
        print('Zkus míň utrácet.')
    elif stastna_a_bohata == 'ani jedno':
        print('To je mi líto.')
    else:
        print('Nerozumím.')
else:
    print('Nerozumím.')
