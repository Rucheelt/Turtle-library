import turtle

sc=turtle.Screen()
sc.bgcolor("Grey")
sc.setup(500,500)
sc.title("Square")

board=turtle.Turtle()

for i in range(4):
    
    board.forward(200)
    board.right(90)
    i=i+1

turtle.done()