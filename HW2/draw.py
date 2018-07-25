# description: This file contains functions to draw rings and diamonds
# author: Salloum, Mariam
# date: 9/7/2015
#
import random
from Tkinter import *

# drawRing: this function draws a ring
# arguments: canvas, x & y coordinates, radius, and color
def drawRing(the_canvas, x, y, radius,width=20, color='red') :
    p1_x,p1_y = x-radius, y-radius
    p2_x,p2_y = x+radius, y+radius
    the_canvas.create_oval(p1_x,p1_y,p2_x,p2_y,fill=color) # outter ring
    the_canvas.create_oval(p1_x+width,p1_y+width,p2_x-width,p2_y-width,fill='white') # inner ring


# drawDiamond: this function draws a diamond
# arguments: canvas, x & y coordinates, radius, and color
def drawDiamond(the_canvas, x, y, width=20, color='blue') :
    p1_x,p1_y = x-width/2, y-width/2
    p2_x,p2_y = x+width/2, y+width/2
    the_canvas.create_rectangle(p1_x,p1_y,p2_x,p2_y,fill=color) # square

# randColor: this function returns a random color
def randColor() :
    r,g,b = int(random.random()*256), int(random.random()*256), int(random.random()*256)
    #print "Random color generated: %d, %d, %d" % (r, g, b)
    return "#%02X%02X%02X" % (r, g, b)
