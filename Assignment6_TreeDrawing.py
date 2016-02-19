import turtle
import random

def drawFern(pen, depth, length, contraction, branches, firstBranchAngle, nextBranchAngle):
    if depth > 0:
        # remember the pen's heading and location
        heading = pen.heading()
        position = pen.position()
        # Draw a branch
        pen.width(depth) # branch width is directly proportional to depth
        pen.forward(length)
        pen.left(firstBranchAngle)
        for i in range(branches):
            pen.width(depth-1)
            drawFern(pen, depth-1, contraction*length, contraction, branches, firstBranchAngle, nextBranchAngle)
            pen.right(nextBranchAngle)

        # restore pen to its start heading and location
        pen.setheading(heading)
        pen.setposition(position)

def drawForest(numOfTrees, xcoord, ycoord):
    while numOfTrees > 0:
        # creates starting location for first tree (within certain bounds)
        p.setx(xcoord)
        p.sety(ycoord)
        p.down()
        drawFern(p, 6, 120, 0.7, 5, 40, 15)
        # re-randomizes the x and y coordinates for a new tree
        xcoord = random.randint(-450,450)
        ycoord = random.randint(-350,-150)
        numOfTrees-=1
        p.up()

p = turtle.Pen() # creates a turtle
p.tracer(False) # this draws faster by not following the turtle animation
p.left(90) # point him up
p.up()

# sets bounds on the turtle's grid for where trees can be drawn
xcoord = random.randint(-450,450)
ycoord = random.randint(-350,-150)

drawForest(20, xcoord, ycoord) # command to draw a forest through functions

p.tracer(True)
turtle.exitonclick()

