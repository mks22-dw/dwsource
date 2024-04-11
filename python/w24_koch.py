import turtle
window = turtle.Screen()
window.setup(600, 600)

def koch_curve(t, depth, size):
    if (depth == 1):
        t.fd(size)
    else:
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)
        t.rt(120)
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)
        

raphael = turtle.Turtle()
raphael.pu()
raphael.goto(-295, 290)
raphael.pd()

window.exitonclick()
        