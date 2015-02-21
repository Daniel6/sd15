import turtle
import random

def drawSnowflakeSide(length, angle, depth):
	x=15
	if depth==0:
		turtle.forward(length)
	else:
		drawSnowflakeSide(length/3.0, angle+x, depth-1)
	turtle.right(angle)
	if depth==0:
		turtle.forward(length)
	else:
		drawSnowflakeSide(length/3.0, angle+x, depth-1)
	turtle.left(angle*2)
	if depth==0:
		turtle.forward(length)
	else:
		drawSnowflakeSide(length/3.0, angle+x, depth-1)
	turtle.right(angle)
	if depth==0:
		turtle.forward(length)
	else:
		drawSnowflakeSide(length/3.0, angle+x, depth-1)

sides=4
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.setpos(-200, -200)
turtle.pendown()
for i in range(sides):
	drawSnowflakeSide(80, 180.0/sides, 3)
	turtle.left(360.0/sides)
turtle.exitonclick()