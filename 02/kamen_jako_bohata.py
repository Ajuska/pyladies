from random import randrange
tah_pocitace = randrange (3)
print (tah_pocitace)
tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_cloveka == 'kámen':
    if tah_pocitace == 0:
        print('Plichta.')
    elif tah_pocitace == 1:
        print('Vyhrála jsi!')
    elif tah_pocitace == 2:
        print('Počítač vyhrál.')
elif tah_cloveka == 'nůžky':
    if tah_pocitace == 0:
        print('Počítač vyhrál.')
    elif tah_pocitace == 1:
        print('Plichta.')
    elif tah_pocitace == 2:
        print('Vyhrála jsi!')
elif tah_cloveka == 'papír':
    if tah_pocitace == 0:
        print('Vyhrála jsi!')
    elif tah_pocitace == 1:
        print('Počítač vyhrál.')
    elif tah_pocitace == 2:
        print('Plichta.')
else:
    print('Nerozumím.')
