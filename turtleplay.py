import turtle

turtle.pensize(2)
turtle.bgcolor('skyblue')
turtle.speed(0)

for i in range(6):
    for colours in ['red', 'brown', 'blue', 'white', 'yellow','orange', 'black','green','red', 'orange']:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
