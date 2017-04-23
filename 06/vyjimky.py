def nacti_cislo():
    while True:
        vstup = input('Zadej číslo:')
        try:
            cislo = int(vstup)
        except ValueError:
            print('To není číslo!')
        except TypeError:
            print('???')
        else:
            return cislo
        finally:
            print('Tohle se provede vždy.')
nacti_cislo()
