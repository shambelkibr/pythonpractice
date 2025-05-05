# this coder using by loop
import turtle

# creeate the scrren object
screen=turtle.Screen()
screen.title("turtle example")
# create the turtle object
t=turtle.Turtle()

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# to eliminate the code redenduncey we can use the  for loop

                                                # to draw squre
# for _ in range(4):  # Loop that runs 4 times
#     t.forward(100)  # Move the turtle forward by 100 units
#     t.left(90)      # Turn the turtle left by 90 degrees

 #                                                thi is for triangle
 
# for _ in range(3):  # Loop that runs 3 times
#     t.forward(100)  # Move the turtle forward by 100 units
#     t.left(120)      # Turn the turtle left by 120 degrees



# t.left(90)       # Turn left by 90 degrees
# t.forward(100)   # Move forward after turning
# turtle.done()



# t.right(90)      # Turn right by 90 degrees
# t.forward(100)   # Move forward after turning
# turtle.done()


# t.penup()         # Lift the pen
# t.forward(100)    # Move forward (no line drawn)
# t.pendown()       # Put the pen down
# t.forward(50)     # Draw a line
# turtle.done()




# t.goto(50, 50)  # Move to (50, 50)
# t.goto(-50, 50) # Move to (-50, 50)
# t.goto(0, 0)    # Move back to the origin
# turtle.done()

'''Moves the turtle to the specified coordinates (x, y) on the screen.
The line is drawn unless the pen is lifted.'''

# t.forward(100)
# t.left(90)
# t.home()  # Return to (0, 0) and reset direction
# turtle.done()



''' Command: circle(radius, extent=None, steps=None)

Draws a circle or arc.
radius: Radius of the circle.
extent (optional): Angle of the arc (e.g., 180 for a half-circle).
steps (optional): Number of line segments to use. '''

# t.circle(50)      # Draw a full circle with radius 50
# turtle.done()


# t.circle(50, 180) # Draw a half-circle (arc)
# turtle.done()

'''Command: speed(value)

Controls the turtle’s movement speed.
"fastest", "fast", "normal", "slow", "slowest", or numbers 0 to 10'''


# t.speed(1)  # Slow speed
# t.forward(100)

# t.speed(10) # Fast speed
# t.forward(100)
# turtle.done()
''' Changes the turtle’s appearance.
Available shapes: "arrow", "turtle", "circle", "square", "triangle", "classic" '''

# t.shape("square")  # Change shape to a turtle
# t.forward(100)
# turtle.done()

'''Command: color(color_name)

Changes the pen color and the turtle’s body color.'''


# t.color("red")    # Change pen and turtle color to blue
# t.forward(100)
# turtle.done()
'''Summary Table of Commands:
Command	Action
forward(distance)----------	--------Move forward
backward(distance)------------------Move backward
left(angle)	------------------------Turn left
right(angle)------------------------Turn right
penup()-----------------------------Lift the pen (no drawing)
pendown()-------------------------Lower the pen (start drawing)
goto(x, y)-------------------------Move to specific coordinates
home()	---------------------------Return to origin and reset
circle(radius)------------------	Draw a circle or arc
speed(value)------------------	Change turtle speed
shape(name)	--------------------Change turtle shape
color(name)----------------------	Change pen and turtle color '''