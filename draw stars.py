import turtle

colors= ['red', 'pink', 'brown', 'orange', 'black', 'purple', 'cyan', 'green']
fill= ['green', 'black', 'orange', 'brown', 'pink', 'cyan', 'purple', 'red']

internal_angle = 36
length = 60

#pen setup
pen = turtle.Turtle()
pen.speed('fastest')
pen.hideturtle()
pen.width(5)

for star in range(8): # 8 stars
	pen.pencolor(colors[star])
	pen.fillcolor(fill[star])

	#draw star
	pen.begin_fill()
	for i in range(5):
		pen.forward(length)
		pen.right(180 - internal_angle) 
	pen.end_fill()

	#space between stars
	pen.penup()
	pen.forward(length+length/3)
	pen.right(45)
	pen.forward(length/3)
	pen.down()

turtle.done()