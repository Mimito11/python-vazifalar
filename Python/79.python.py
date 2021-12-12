import turtle

star = turtle.Turtle()

for i in range(5):
    star.forward(200)
    star.right(144)

# turtle.done()

for i in range(10):
    star.pencolor("red")
    star.setposition(0,1)
    star.forward(200)
    star.right(150)
turtle.done()
