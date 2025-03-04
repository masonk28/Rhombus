import turtle

screen = turtle.Screen()


t = turtle.Turtle()

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("yellow")

t.speed(0)
t.setheading(135)
t.fillcolor("cyan")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.speed(0)
t.setheading(45)
t.fillcolor('brown')
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

t.hideturtle()
turtle.done()