
import turtle

window = turtle.Screen()

amo = turtle.Turtle()

amo.speed(10)

for i in range(360):
    amo.right(50)
    amo.backward(50)
    amo.right(50)
    amo.left(50)
    amo.forward(25)
    amo.right(50)
    amo.forward(50)
    amo.backward(50)
    amo.left(50)
    amo.backward(50)
