import turtle


def draw_square(t, size):
    i = 0
    while i < 4:
        t.fd(size)
        t.rt(90)
        i+= 1

def draw_spiral0(t, size):
    while (size >= 5):
        t.fd(size)
        t.rt(90)
        size-= 5
        
def draw_spiral1(t, size, angle):
    if (size >= 5):
        t.fd(size)
        t.rt(angle)
        draw_spiral1(t, size-5, angle)


window = turtle.Screen()
window.setup(600, 600)

donatello = turtle.Turtle()
donatello.pu()
donatello.setx(-300)
donatello.sety(300)
donatello.pd()
draw_square(donatello, 100)

donatello.pu()
donatello.sety(100)
donatello.pd()
draw_spiral0(donatello, 200)


#draw_spiral1(donatello, 200, 10)

window.exitonclick()