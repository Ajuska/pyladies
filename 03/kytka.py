from turtle import shape, forward, left, right, exitonclick
shape('turtle')
n = 10
for strana in range(18): #kvet
    for j in range(4):
        forward(50)
        left(90)
    left(20)
right(90)
forward(100) #jde dolu - stonek
for stonek_listky in range(0, 12, 4): #udela cely stonek
    right(140)
    for listek in range(2): #pravy listeky
        for jedna_strana in range(n + stonek_listky):
            left(5)
            forward(10)
        right(230 + stonek_listky * 5)
    left(140)
    forward(20 + stonek_listky * 5)

    left(75)
    for listek in range(2): #levy listeky
        for jedna_strana in range(n + stonek_listky):
            left(5)
            forward(10)
        right(230 + stonek_listky * 5)
    right(75)
    forward(20 + stonek_listky * 5)

exitonclick()
