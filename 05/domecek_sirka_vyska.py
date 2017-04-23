from turtle import shape, forward, left, right, exitonclick
from math import sqrt, acos, degrees

shape('turtle')

def vypocti_preponu(sirka, vyska):
    return sqrt(sirka**2+vyska**2)

def vykresli_domecek(sirka, vyska):
    prepona = vypocti_preponu(sirka, vyska)
    striska = vypocti_preponu(sirka, vyska)/2
    uhel_1 = 180 - degrees(acos(vyska/prepona))
    uhel_2 = (180 - uhel_1)*2
    left(90)
    forward(vyska)
    right(90)
    forward(sirka)
    right(90)
    forward(vyska)
    right(uhel_1)
    forward(prepona)
    right(uhel_2)
    forward(striska)
    right(180-uhel_2)
    forward(striska)
    right(uhel_2)
    forward(prepona)
    left(180-(90-(180-uhel_1)))
    forward(sirka+20)

vykresli_domecek(20, 20)
vykresli_domecek(10, 90)
vykresli_domecek(100, 30)

exitonclick()
