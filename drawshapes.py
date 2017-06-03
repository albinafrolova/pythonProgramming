import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()
    
def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(3)
    i = 0
    while (i < 4):
      brad.forward(100)
      brad.right(90)
      i = i + 1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("classic")
    angie.color("black")
    angie.circle(100)

def draw_triangle():
    lily = turtle.Turtle()
    lily.shape("circle")
    lily.color("blue")
    i = 0
    while (i < 3):
       lily.forward(100)
       lily.left(120)
       i = i + 1 

draw_shapes() 
