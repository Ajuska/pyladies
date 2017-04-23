def pohlavi(prijmeni):
    "na zakladě zadání příjemní pozná pohlaví"
    koncovka = prijmeni[-3:]
    if  koncovka == 'ová' or koncovka == "ova" or koncovka == 'á':
    #if  prijmeni.endswith('ová') or prijmeni.endswith('á')
        return 'žena'
    else:
        return 'muž'

prijmeni = input('Zadej své příjmení:')
print("Vím že jsi " + pohlavi(prijmeni))
