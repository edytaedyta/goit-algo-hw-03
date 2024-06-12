import turtle

def draw_koch_curve(t, size, level):
    if level == 0:
        t.forward(size)
    else:
        size /= 3.0
        draw_koch_curve(t, size, level-1)
        t.left(60)
        draw_koch_curve(t, size, level-1)
        t.right(120)
        draw_koch_curve(t, size, level-1)
        t.left(60)
        draw_koch_curve(t, size, level-1)

def draw_koch_snowflake(t, size, level):
    for _ in range(3):
        draw_koch_curve(t, size, level)
        t.right(120)

def main():
    # Set up the turtle graphics window
    window = turtle.Screen()
    window.setup(width=1000, height=1000)
    window.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-300, 200)
    t.pendown()
    t.pencolor("white")
    
    # Set the level of recursion by the users
    level = int(input("Enter the level of recursion (e.g., 3): "))
    
    # Draw the Koch snowflake
    draw_koch_snowflake(t, 600, level)
    
    # Hide the turtle and display the window
    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()