from turtle import shape, forward, left, right, exitonclick
from math import sqrt
shape('turtle')

def vypocti_preponu(strana):
    return sqrt(strana**2+strana**2)

def vykresli_domecek(strana):
    prepona = vypocti_preponu(strana)
    striska = prepona/2
    left(90)
    forward(strana)
    right(90)
    forward(strana)
    right(90)
    forward(strana)
    right(135)
    forward(prepona)
    right(90)
    forward(striska)
    right(90)
    forward(striska)
    right(90)
    forward(prepona)
    left(135)
    forward(strana+20)

vykresli_domecek(20)
vykresli_domecek(50)
vykresli_domecek(100)

exitonclick()
