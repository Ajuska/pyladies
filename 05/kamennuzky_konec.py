from random import randrange
tah_pocitace = randrange(3)
if tah_pocitace == 0:
    tah_pocitace = 'kámen'
elif tah_pocitace == 1:
    tah_pocitace = 'nůžky'
else:
    tah_pocitace = 'papír'

while True:
    tah_cloveka = input('kámen, nůžky, papír nebo konec?')
    if tah_cloveka == 'konec':
        break
    if tah_cloveka == 'kámen' or tah_cloveka == 'nůžky' or tah_cloveka == 'papír':
        if tah_cloveka == tah_pocitace:
            print('Plichta.')
        elif (tah_cloveka == 'kámen' and tah_pocitace == 'nůžky'
            or tah_cloveka == 'nůžky' and tah_pocitace == 'papír'
            or tah_cloveka == 'papír' and tah_pocitace == 'kámen'):
            print('Vyhrála jsi!')
        else:
            print('Počítač vyhrál.')
        print('Počítač táhl', tah_pocitace)
    else:
        print('Nerozumím.')
