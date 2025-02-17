#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(myTurtle, sides):
    angle = 360 / sides
    for s in range(sides):
        myTurtle.forward(50)
        myTurtle.right(angle)


def fillCorner(myTurtle, corner):
    myTurtle.up()
    myTurtle.goto(-100, 100)
    myTurtle.down()
    
    #big square
    drawSquare(myTurtle, 200)
    
    #move to position
    if corner == 2:
        myTurtle.forward(100)
    if corner == 3:
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.left(90)
    
    myTurtle.begin_fill()
    drawSquare(myTurtle, 100)
    myTurtle.end_fill()

def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
