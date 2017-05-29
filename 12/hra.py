import pyglet
import math
from pyglet import gl
window = pyglet.window.Window()

ACCELERATION = 100
ROTATION_SPEED = 200

spaceship_picture = pyglet.image.load("/home/aja/pyladies/12/obrazky/PNG/playerShip1_blue.png")
spaceship_picture.anchor_x = spaceship_picture.width // 2
spaceship_picture.anchor_y = spaceship_picture.height // 2
batch = pyglet.graphics.Batch()

pressed_keys = set()

class SpaceObject:
    def __init__(self, window):
        self.x = 0
        self.x = 0
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        self.window = window

class Spaceship(SpaceObject):
    def __init__(self, window):
        super().__init__(window)
        self.x = window.width / 2
        self.y = window.height / 2
        self.sprite = pyglet.sprite.Sprite(spaceship_picture, batch=batch)


    def tick(self, t):
        rotation_radians = math.radians(self.rotation)
        if pyglet.window.key.UP in pressed_keys:
            self.x_speed = self.x_speed + math.cos(rotation_radians) * ACCELERATION * t
            self.y_speed = self.y_speed + math.sin(rotation_radians) * ACCELERATION * t
        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation = self.rotation - ROTATION_SPEED * t
        if pyglet.window.key.LEFT in pressed_keys:
            self.rotation = self.rotation + ROTATION_SPEED * t

        self.x = self.x + self.x_speed * t
        self.y = self.y + self.y_speed * t

        while self.x > self.window.width:
            self.x = self.x - self.window.width
        while self.y > self.window.height:
            self.y = self.y - self.window.height
        while self.x < 0:
            self.x = self.x + self.window.width
        while self.y < 0:
            self.y = self.y + self.window.height

        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - self.rotation

objects = []
for i in range(1):
    spaceship = Spaceship(window)
    spaceship.rotation = i * 10
    objects.append(spaceship)

def on_draw():
    window.clear()

    for x in -window.width, 0, window.width:
        for y in -window.height, 0, window.height:
            gl.glPushMatrix()
            gl.glTranslatef(x, y, 0)
            for obj in objects:
                batch.draw()
            gl.glPopMatrix()

def tick(t):
    for obj in objects:
        obj.tick(t)

def on_key_press(sym, mod):
    pressed_keys.add(sym)
    print(pressed_keys)

def on_key_release(sym, mod):
    pressed_keys.discard(sym)
    print(pressed_keys)

pyglet.clock.schedule_interval(tick, 1/60)


window.push_handlers(
    on_draw=on_draw,
    on_key_press=on_key_press,
    on_key_release=on_key_release,
)

pyglet.app.run()
