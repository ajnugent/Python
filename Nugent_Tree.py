#Jackie Nugent 
#Extra Credit Graphics Tree 
#CS 2050

import random
import turtle

#Passes the size of the tree 
def drawTree(size, myTurtle):
    
    #Thickness of pensize
    myTurtle.pensize(size / 10)

    #Change the color of the branches when they reach a certain size 
    
    if size < random.randint(1,2) * 15:
        
        myTurtle.color("green")
    
        
    else:
       
        myTurtle.color("brown")

    if size > 5:
        
        myTurtle.forward(size)
        myTurtle.left(25)
        
        #Left hand side of branch 
        drawTree(size - random.randint(10, 20), myTurtle)
        
        myTurtle.right(50)
        
        #Right hand side of branch
        drawTree(size - random.randint(10, 20), myTurtle)
        
        myTurtle.left(25)
        myTurtle.penup()
        myTurtle.backward(size)
        myTurtle.pendown()


if __name__ == "__main__":
    
    window = turtle.Screen()
    window.bgcolor("black")

    myTurtle = turtle.Turtle()
    myTurtle.color("brown", "blue")
    
    #Makes sure the tree is positioned upright
    myTurtle.left(90)
    myTurtle.speed(0)
    myTurtle.penup()
    
    #Center the tree in the window 
    myTurtle.setpos(0, -250)
    myTurtle.pendown()

    drawTree(110, myTurtle)

window.exitonclick()