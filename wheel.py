import turtle

turtle.penup()

def drawCircle(tcolor, pen_color, scolor, radius, mv):
    turtle.pencolor(pen_color)  # not filling but makes body of turtle this colo
    turtle.fillcolor(tcolor)  # not filling but makes body of turtle this colo
    turtle.begin_fill()
    turtle.right(90)    # Face South
    turtle.forward(radius)   # Move one radius
    turtle.right(270)   # Back to start heading
    turtle.pendown()    # Put the pen back down
    turtle.circle(radius)    # Draw a circle
    turtle.penup()      # Pen up while we go home
    turtle.end_fill() # End fill.
    turtle.home()       # Head back to the start pos


def drawHexagon(side_length, pen_color):
    polygon = turtle.Turtle() 
    polygon.pencolor(pen_color) 
    num_sides = 6
    angle = 360.0 / num_sides 
    polygon.penup()      # Pen up while we go home
    polygon.left(120)
    polygon.forward(side_length) 
    polygon.right(120) 
    polygon.pendown()      # start drawing hexagon
    for i in range(num_sides): 
	    polygon.forward(side_length) 
	    polygon.right(angle) 
    polygon.pencolor("white") 
    polygon.fillcolor("white")
    polygon.penup()
    polygon.home()
    

drawCircle("blue", "blue", "black", 200, 30)
print (" 2 ")
drawCircle("white", "white", "black", 150, 30)
drawHexagon(200, "white")
drawHexagon(150, "blue")

	


turtle.exitonclick() 