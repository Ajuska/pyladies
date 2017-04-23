from turtle import shape, forward, left, right, exitonclick
from math import sqrt
shape('turtle')

strana = 50
prepona = sqrt(strana**2+strana**2)
striska = prepona/2

for domek in range(6):
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

exitonclick()
