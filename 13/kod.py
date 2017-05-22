from machine import Pin, PWM
from time import sleep

pin_led = Pin(14, Pin.OUT)
pwm = PWM(pin_led, freq=50,
          duty=200)
sleep(1)
pwm.duty(500)

pin_piezo = Pin(13, Pin.OUT)

pwm = PWM(pin_piezo, freq=65,
          duty=1012)

#duty muze byt od 0 do 1024

#while True:
#    pin_led.value(1)
#    sleep(1/10)
#    pin_led.value(0)
#    sleep(1/10)
