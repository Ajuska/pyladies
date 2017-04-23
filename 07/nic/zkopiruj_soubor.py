jmeno_souboru = input('Zadej jmeno souboru s priponou:')
nove_jmeno_souboru = input('Zadej nove jmeno souboru s priponou:')

with open(jmeno_souboru, encoding='utf-8') as zdroj:
    with open(nove_jmeno_souboru, mode='w', encoding='utf-8') as soubor:
        soubor.write(zdroj.read())
        soubor.write('...byly žily dvě jeskyňky')
