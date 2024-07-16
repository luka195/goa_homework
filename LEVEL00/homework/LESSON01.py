from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

# drawing a door
color ("red")
begin_fill()

forward(50)
left(90)

forward(100)
right(90)

forward(100)
right(90)
forward(100)
end_fill()
# i am done with the door
penup()
goto(0, 200)


pendown()


color("red")
begin_fill()


left(150)
forward(200)







right(120)
forward(200)
end_fill()
penup()
goto(30, 150)
pendown()

left(60)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

penup()
goto(120, 150)
pendown()

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)



exitonclick()
