import turtle
window = turtle.Screen()
window.setup(600, 600)

def tree(t, depth, size, angle):
    if depth == 0:
        t.fd(size)
        t.bk(size)
    else:
        t.fd(size)
        t.rt(angle)
        tree(t, depth-1, size, angle)
        t.lt(2 * angle)
        tree(t, depth-1, size, angle)
        t.rt(angle)
        t.bk(size)


leonardo = turtle.Turtle()
leonardo.lt(90)
leonardo.pd()
tree(leonardo, 4, 50, 20)

window.exitonclick()
