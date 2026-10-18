
import turtle
import colorsys

screen = turtle.Screen()
screen.title("Turtle Pattern Generator and Fractal Renderer")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

# Generate RGB colors dynamically
def get_color(i, total):
    return colorsys.hsv_to_rgb(i / total, 1.0, 1.0)

# Draw a Koch curve recursively
def koch_curve(length, level):
    if level == 0:
        pen.forward(length)
    else:
        koch_curve(length / 3, level - 1)
        pen.left(60)
        koch_curve(length / 3, level - 1)
        pen.right(120)
        koch_curve(length / 3, level - 1)
        pen.left(60)
        koch_curve(length / 3, level - 1)

# Draw a Koch snowflake
def koch_snowflake(length, level):
    for _ in range(3):
        koch_curve(length, level)
        pen.right(120)

# Draw a colorful spiral
def spiral():
    for i in range(150):
        pen.pencolor(get_color(i, 150))
        pen.forward(i * 2)
        pen.right(91)

print("Turtle Pattern Generator")
print("1. Koch Snowflake")
print("2. Colorful Spiral")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    level = int(input("Enter fractal level (0-4): "))
    level = max(0, min(level, 4))

    pen.penup()
    pen.goto(-200, 120)
    pen.pendown()

    pen.pencolor("cyan")
    koch_snowflake(400, level)

elif choice == "2":
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

    spiral()

else:
    print("Invalid choice!")

screen.update()
screen.mainloop()
