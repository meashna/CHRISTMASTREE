from turtle import *

speed(0)

penup()
goto(0, -250)
pendown()

penup()
goto(-15, -50)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()

y = -50
width = 240
height = 25

while width > 20:
    width = width - 30  # Make the tree get smaller as it goes up in height
    x = 0 - width / 2  # Set the starting x-value of each level of the tree
    color("green")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

    y = y + height

# Star
penup()
goto(-15, 150)
pendown()
color("yellow")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()

# Message
penup()
goto(-130, -150)
color("red")
write("MERRY CHRISTMAS by ASHNA T", font=("Arial", 10, "bold"))

hideturtle()
