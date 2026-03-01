import turtle


screen = turtle.Screen()
#first turtle variables and functions
t1 = turtle
t1.penup()
t1.pencolor("white")
t1.bgcolor("navy")
t1.fillcolor("white")
screen.bgpic("istockphoto-178149253-612x612.gif")


stars = []

def list_stars(x,y):
    stars.append((x,y))

def mouse_star(x,y):

    t1.goto(x,y)

    t1.begin_fill()
    t1.pendown()
    for i in range(4):

        t1.forward(8)
        t1.left(90)
    t1.fillcolor("white")

    t1.end_fill()

screen.onclick(list_stars)

def draw_stars():
    if len(stars) > 0:
        mouse_star(stars[0][0],stars[0][1])
        stars.pop(0)
    screen.ontimer(draw_stars,100)
screen.ontimer(draw_stars,100)

t1.done()