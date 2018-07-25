# description: This is to draw random rings

# author : WANG, ZEZHI

# date: Sep,11 2015

import random

from Tkinter import *

print "Please input as : randomRings(n)"

window=Tk()
the_canvas=Canvas(window,width=400,height=400)
the_canvas.grid(row=0,column=0)

def randColor() :
    r,g,b = random.randint(0,256), random.randint(0,256), random.randint(0,256)
    return "#%02X%02X%02X" % (r, g, b)

def randomRings(n):
    for i in range(0, n):
        x,y = random.randint(1,400),random.randint(1,400)
        radius = random.randint(1,200)
        width = random.randint(1,radius)
        drawRing(x,y,radius,width)
    window.mainloop()

def drawRing(x,y,radius,width) :
    p1_x,p1_y = x - radius, y - radius
    p2_x,p2_y = x + radius, y + radius
    the_canvas.create_oval(p1_x,p1_y,p2_x,p2_y,fill = randColor()) 
    the_canvas.create_oval(p1_x+width,p1_y+width,p2_x-width,p2_y-width,fill='white') 

