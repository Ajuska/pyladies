from turtle import shape, forward, left, right, exitonclick
shape('turtle')
n = 500
for i in range(n):
    left(12)
    #forward(i*5) # 0 5 10 15 20 25 30
    forward(0.1 + i/30)



exitonclick()
