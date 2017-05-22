from machine import Pin
from neopixel import NeoPixel

pin = Pin(2, Pin.OUT)
np = NeoPixel(pin, 8)
np[0] = 20, 20, 20
np[1] = 102, 255, 51
np[2] = 0, 25, 25
np[3] = 255, 51, 102
np.write()
