import pyglet
import math
from pyglet import gl
from random import randrange, uniform
window = pyglet.window.Window()

ACCELERATION = 100
ROTATION_SPEED = 200

ASTEROID_SPEED = 200
ASTEROID_ROTATION_SPEED = 100


def load_image(filename):
    picture = pyglet.image.load(filename)
    picture.anchor_x = picture.width // 2
    picture.anchor_y = picture.height // 2
    return picture


spaceship_picture = load_image("/home/aja/pyladies/12/obrazky/PNG/playerShip1_blue.png")
asteroid_picture = load_image("/home/aja/pyladies/12/obrazky/PNG/Meteors/meteorBrown_big1.png")
laser_picture = load_image("/home/aja/pyladies/12/obrazky/PNG/Lasers/laserBlue06.png")
batch = pyglet.graphics.Batch()

pressed_keys = set()


def draw_circle(x, y, radius):
  iterations = 20
  s = math.sin(2*math.pi / iterations)
  c = math.cos(2*math.pi / iterations)

  dx, dy = radius, 0

  gl.glBegin(gl.GL_LINE_STRIP)
  for i in range(iterations+1):
      gl.glVertex2f(x+dx, y+dy)
      dx, dy = (dx*c - dy*s), (dy*c + dx*s)
  gl.glEnd()


def distance(a, b, wrap_size):
    """Distance in one direction (x or y)"""
    result = abs(a - b)
    if result > wrap_size / 2:
        result = wrap_size - result
    return result

def overlaps(a, b):
    """Returns true iff two space objects overlap"""
    distance_squared = (distance(a.x, b.x, window.width) ** 2 +
                        distance(a.y, b.y, window.height) ** 2)
    max_distance_squared = (a.radius + b.radius) ** 2
    return distance_squared < max_distance_squared

class SpaceObject:
    def __init__(self, window):
        self.x = 0
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        self.rotation_speed = 0
        self.radius = 35
        self.window = window


    def hit_by_spaceship(self, spaceship):
        pass

    def hit_by_laser(self, laser):
        pass


    def tick(self, t):
        #Movement
        self.x = self.x + self.x_speed * t
        self.y = self.y + self.y_speed * t
        self.rotation = self.rotation + self.rotation_speed * t        #Wrap at the edges of the screen
        while self.x > self.window.width:
            self.x = self.x - self.window.width
        while self.y > self.window.height:
            self.y = self.y - self.window.height
        while self.x < 0:
            self.x = self.x + self.window.width
        while self.y < 0:
            self.y = self.y + self.window.height
        #Update the sprite
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - self.rotation

    def delete(self):
        objects.remove(self)
        self.sprite.delete()

class Asteroid(SpaceObject):
    def __init__(self, window):
        super().__init__(window)
        self.sprite = pyglet.sprite.Sprite(asteroid_picture, batch=batch)
        self.is_asteroid = True

        self.x_speed = uniform(-ASTEROID_SPEED, ASTEROID_SPEED)
        self.y_speed = uniform(-ASTEROID_SPEED, ASTEROID_SPEED)
        self.radius = 40

        if randrange(2) == 0:
            self.x = uniform(0, window.width)
        else:
            self.y = uniform(0, window.height)

        self.rotation_speed = uniform(-ASTEROID_ROTATION_SPEED,
                                        ASTEROID_ROTATION_SPEED)

    def hit_by_spaceship(self, spaceship):
        spaceship.delete()

    def hit_by_laser(self, laser):
        self.delete()
        laser.delete()





class Spaceship(SpaceObject):
    def __init__(self, window):
        super().__init__(window)
        self.x = window.width / 2
        self.y = window.height / 2
        self.sprite = pyglet.sprite.Sprite(spaceship_picture, batch=batch)
        self.time_from_last_laser = 0

    def tick(self, t):
        #Heading in radlans
        rotation_radians = math.radians(self.rotation)
        #Keybord control - speed up or turn
        if pyglet.window.key.UP in pressed_keys:
            self.x_speed = self.x_speed + math.cos(rotation_radians) * ACCELERATION * t
            self.y_speed = self.y_speed + math.sin(rotation_radians) * ACCELERATION * t
        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation = self.rotation - ROTATION_SPEED * t
        if pyglet.window.key.LEFT in pressed_keys:
            self.rotation = self.rotation + ROTATION_SPEED * t
        if pyglet.window.key.SPACE in pressed_keys:
            if self.time_from_last_laser > 1/3:
                laser = Laser(self)
                objects.append(laser)
                self.time_from_last_laser = 0

        self.time_from_last_laser = self.time_from_last_laser + t

        #Slow down gradually
        self.x_speed = self.x_speed / 1.5 ** t
        self.y_speed = self.y_speed  / 1.5 ** t

        super().tick(t)

        for obj in list(objects):
            if overlaps(obj, self):
                obj.hit_by_spaceship(self)


class Laser(SpaceObject):
    def __init__(self, parent):
        super().__init__(parent.window)
        self.sprite = pyglet.sprite.Sprite(laser_picture, batch=batch)
        self.x = parent.x
        self.y = parent.y
        self.x_speed = parent.x_speed
        self.y_speed = parent.y_speed
        self.rotation = parent.rotation
        self.radius = 20

        rotation_radians = math.radians(self.rotation)
        self.x_speed = parent.x_speed + 500 * math.cos(rotation_radians)
        self.y_speed = parent.y_speed + 500 * math.sin(rotation_radians)

    def tick(self, t):
        super().tick(t)
        for obj in list(objects):
            if overlaps(obj, self):
                obj.hit_by_laser(self)




#Create initial objects
objects = []
for i in range(1):
    spaceship = Spaceship(window)
    spaceship.rotation = i * 10
    objects.append(spaceship)

asteroid = Asteroid(window)
objects.append(asteroid)


def on_draw():
    window.clear()
    for x in -window.width, 0, window.width:
        for y in -window.height, 0, window.height:
            gl.glPushMatrix()
            gl.glTranslatef(x, y, 0)
            batch.draw()
            gl.glPopMatrix()

    """Vykresli kolecka"""
    #for obj in objects:
    #    draw_circle(obj.x, obj.y, obj.radius)

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


rozdelit asteroid po zasahu na dva mensi
laser po urcite dobe zmizi
