import turtle

# Setup the turtle
screen = turtle.Screen()
screen.title("Multiple Shapes with Turtle")
t = turtle.Turtle()
t.speed(5)  # Set a moderate speed

# Function to draw a polygon
def draw_polygon(sides, length, color):
    t.color(color)  # Set turtle color
    angle = 360 / sides  # Angle to turn at each vertex
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

# Draw a square
t.penup()
t.goto(-150, 0)  # Move to a new position
t.pendown()
draw_polygon(4, 100, "blue")  # 4 sides, length 100, color blue

# Draw a triangle
t.penup()
t.goto(50, 0)  # Move to a new position
t.pendown()
draw_polygon(3, 100, "red")  # 3 sides, length 100, color red

# Draw a hexagon
t.penup()
t.goto(-50, -150)  # Move to a new position
t.pendown()
draw_polygon(6, 80, "green")  # 6 sides, length 80, color green

# Finish
turtle.done()
