vzory = (
    ('x-x', 1),
    ('-x-', 0),
    ('xx-', 2),
    #...ATD...
)

def tah_pocatace_x(herni_pole):
    for vzor, poloha in vzory:
        if vzor in herni_pole:
            a = herni_pole.index(vzor) + poloha
            return tah(herni_pole, a, 'x')
