
import turtle


a=turtle.Turtle()
b=turtle.Turtle()

a.color('red')
b.color('yellow')

for i in range(361):
    a.forward(1)
    a.left(1)
    
    b.forward(1)
    b.right(1)
    
turtle.done()
