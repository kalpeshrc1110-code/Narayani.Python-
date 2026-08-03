import turtle
import time
p = turtle.Turtle()
turtle.Screen().bgcolor ("umber")
turtle.Screen().setup (500.400)
num_side = 6
side_lenth = 70
angle = 360.00 / num_side
for i in range (num_side):
    p.forward(side_lenth)
    p.right(angle)
    time.sleep (1)
p.forward (angle)
for i in range (4):
    p.forward(side_lenth)
    p.right(angle)
    time.sleep (1)

turtle.draw()