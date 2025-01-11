import turtle

sc=turtle.Screen()
sc.bgcolor("Grey")
sc.setup(500,500)
sc.title("Star")

board=turtle.Turtle()

#first triangle 

board.forward(200)
board.left(120)
board.forward(200)
board.left(120)
board.forward(200)

board.penup()
board.right(150)
board.forward(100)
board.pendown()
board.right(90)
board.forward(200)
board.right(120)
board.forward(200)
board.right(120)
board.forward(200)

turtle.done