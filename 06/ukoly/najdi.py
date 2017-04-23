def najdi_symboly(herni_pole, symbol_hrace):
    list_pozic_symbolu = list()
    for index, symbol in enumerate(herni_pole):
        print(index, symbol)
        if symbol == symbol_hrace:
            list_pozic_symbolu.append(index)
    return list_pozic_symbolu
