#Jackie Nugent
#Extra credit Spiral
#CS 2050

import turtle

def drawSpiral(radius):
    
    # x and y coordinates 
    xCor = turtle.xcor()
    yCor = turtle.ycor()
    
    #The distance from the center
    expand = 1
    
    while True:
        
        turtle.forward(expand)
        turtle.left(10)
        expand += 0.1
        
        if turtle.distance(xCor, yCor) > radius:
            break
        
if __name__ == "__main__":
    
    drawSpiral(200)