import turtle
window = turtle.Screen()
window.setup(600, 600)

def triangle(t, size):
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)

def sierpinski(t, depth, size, scale_factor=1):
    if depth == 1:
        triangle(t, size)
    else:
        sierpinski(t, depth-1, size/2)
        t.fd(size/2)
        sierpinski(t, depth-1, size/2)
        t.bk(size/2)
        t.lt(60)
        t.fd(size/2)
        t.rt(60)
        sierpinski(t, depth-1, size/2)
        t.rt(120)
        t.fd(size/2)
        t.lt(120)

michelangelo = turtle.Turtle()
michelangelo.pu()
michelangelo.speed(0)
michelangelo.goto(-295, 0)
michelangelo.pd()
sierpinski(michelangelo, 5, 200)

window.exitonclick()
