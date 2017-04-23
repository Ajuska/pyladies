from random import randrange
tah_pocitace = randrange(3)
if tah_pocitace == 0:
    tah_pocitace = 'kámen'
elif tah_pocitace == 1:
    tah_pocitace = 'nůžky'
else:
    tah_pocitace = 'papír'

tah_cloveka = input('kámen, nůžky, nebo papír?')
print('Počítač táhl', tah_pocitace)

if tah_cloveka == 'kámen':
    if tah_pocitace == 'kámen':
        print('Plichta.')
    elif tah_pocitace == 'nůžky':
        print('Vyhrála jsi!')
    elif tah_pocitace == 'papír':
        print('Počítač vyhrál.')
elif tah_cloveka == 'nůžky':
    if tah_pocitace == 'kámen':
        print('Počítač vyhrál.')
    elif tah_pocitace == 'nůžky':
        print('Plichta.')
    elif tah_pocitace == 'papír':
        print('Vyhrála jsi!')
elif tah_cloveka == 'papír':
    if tah_pocitace == 'kámen':
        print('Vyhrála jsi!')
    elif tah_pocitace == 'nůžky':
        print('Počítač vyhrál.')
    elif tah_pocitace == 'papír':
        print('Plichta.')
else:
    print('Nerozumím.')
