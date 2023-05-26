from turtle import*
exitonclick()
speed(300)
penup()
color("light blue")
goto(-250, 250)
pendown()
begin_fill()
forward(500)
right(90)
forward(400)
right(90)
forward(500)
right(90)
forward(400)
right(90)
end_fill()
penup()
goto(-50, 150)
color("yellow")
begin_fill()
for i in range(50):
    left(100)
    forward(70)
end_fill()
penup()


goto(-150, 50)
right(50)
pendown()
begin_fill()
color("lightyellow")
forward(200)
right(90)

forward(130)
right(90)

forward(200)
right(90)

forward(130)
right(90)

end_fill()
penup()
forward(50)
begin_fill()
pendown()
left(90)
forward(100)
right(90)
forward(150)
right(90)
forward(100)
end_fill()


penup()
begin_fill()
right(180)
forward(100)
pendown()
left(90)
forward(120)
right(90)
forward(100)
right(90)
forward(120)
right(90)
forward(10)
end_fill()

penup()
goto(250, -250)
color("green")
pendown()
width(200)
forward(500)





from turtle import*
from random import*
exitonclick()
a = Turtle()
b = Turtle()
c = Turtle()

a.shape("turtle")
b.shape("turtle")
c.shape("turtle")



a.color("blue")
a.penup()
a.goto(0, -150)
a.pendown()
b.color("yellow")
b.xcor()
b.up()
b.goto(0, -170)
b.down()
c.color("red")
c.up()
c.goto(0, -190)
c.down()

while a.xcor() < 200 and b.xcor() < 200:
    a.forward(randint(0, 7))
    b.forward(randint(0, 7))
    c.forward(randint(0, 7))

if a.xcor() > b.xcor() > c.xcor():
    a.write("Я переміг!")

if b.xcor() > a.xcor() > c.xcor():
    b.write("Я переміг!")

if c.xcor() > a.xcor() > b.xcor():
    c.write("Я переміг!")


