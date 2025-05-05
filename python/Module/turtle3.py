# import turtle
# sham=turtle.Turtle()

# sham.forward(100)
# sham. left(90)
# sham.forward(100)
# sham. left(90)
# sham.forward(100)
# sham. left(90)
# sham.forward(100)
# sham. left(90)
# Import the turtle module
import turtle

# Create a screen object
screen = turtle.Screen()
screen.title("Turtle Example")

# Create a turtle object
t = turtle.Turtle()

# Customize the turtle
t.shape("turtle")  # Turtle shape
t.color("blue")    # Turtle color
t.pensize(3)       # Pen size

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.left(90)      # Turn left by 90 degrees

# Finish
screen.mainloop()
