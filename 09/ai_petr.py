def tah_pocitace(pole, symbol):
    if '-' not in pole:
        raise ValueError('Plne pole')

    if symbol == 'x':
        druhy_symbol = 'o'
    else:
        druhy_symbol = 'x'

    # MM- -> MMM
    # M-M -> MMM

    # JJ -> JJM

    for sablona in 'MM!', !MM M!M JJ! !JJ J!J -!M- M!- =!M -M! J!- -!J:
        co_hledam = sablona.replace('M', symbol)
        co_hledam = co_hledam.replace('J', druhy_symbol)
        co_hledam = co_hledam.replace('!', '-')

        za_co_to_zamenim = sablona.replace('M', symbol)
        za_co_to_zamenim = za_co_to_zamenim.replace('J', druhy_symbol)
        za_co_to_zamenim = za_co_to_zamenim.replace('!', symbol)

        if co_hledam in pole:
            index = pole.index(co_hledam)
            index_vykricniku = sablona.index('!')
            return tah(pole, index_vykricniku + symbol)
