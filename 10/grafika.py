import pyglet
import math
window = pyglet.window.Window()

def tik(t):
    had.x = had.x + t * 20
    had.y = 20 + 20 * math.sin(had.x / 5)
    print(t)

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    print(text)

obrazek = pyglet.image.load('caticorn.jpg')
obrazek2 = pyglet.image.load('unicorn.png')
had = pyglet.sprite.Sprite(obrazek)

def zamen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zamen2, 1)

def zamen2(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zamen, 1)

pyglet.clock.schedule_once(zamen, 1)

had.x = 1
had.y = 200

def vykresli():
    window.clear()
    had.draw()

def klikni(x, y, tlacitko, mod):
    had.x = x
#    had.y = y


window.push_handlers(
        on_text=zpracuj_text,
        on_draw=vykresli,
        on_mouse_press=klikni
    )

pyglet.app.run()
print('Hotovo!')
