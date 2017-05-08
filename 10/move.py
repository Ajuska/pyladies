import pyglet
window = pyglet.window.Window()

obrazek = pyglet.image.load('unicorn.png')
unicorn = pyglet.sprite.Sprite(obrazek)

def vykresli():
    window.clear()
    unicorn.draw()

def tik(t):
    unicorn.rotation = unicorn.rotation + 40 * t




def posun(text):
    """Posune obrazek podle zmackute klavesy"""
    if text == 'd':
        unicorn.x = unicorn.x + 20
    elif text == 'a':
        unicorn.x = unicorn.x - 20
    elif text == 'w':
        unicorn.y = unicorn.y + 20
    elif text == 's':
        unicorn.y = unicorn.y - 20
    elif text == 'r':
        pyglet.clock.schedule_interval(tik, 1/30)
    elif texcdt == 't':
        pyglet.clock.unschedule(tik)

window.push_handlers(
        on_draw=vykresli,
        on_text=posun
    )
pyglet.app.run()
print('Hotovo!')
