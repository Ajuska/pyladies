from turtle import shape, forward, left, right, exitonclick
shape('turtle')

n = int(input('zadej cislo'))
uhel = 180-(180*(1-2/n))
print(uhel)


for strana in range(n):
    forward(200/n)
    print(200/n)
    left(uhel)

exitonclick()
