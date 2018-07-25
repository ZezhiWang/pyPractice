# description: This is to draw diamonds

# author : WANG, ZEZHI

# date: Sep,11 2015

import random

from Tkinter import *

print "Please input as: diamond(n)"

window=Tk()
the_canvas=Canvas(window,width=400,height=400)
the_canvas.grid(row=0,column=0)

def diamond(n):
    w = int (400 / n)
    for i in range (0,n):
        drawDiamond(i*w,400-i*w,w)
    window.mainloop()

def drawDiamond(x,y,w) :
    p_x,p_y = x+w, y-w
    the_canvas.create_rectangle(x,y,p_x,p_y,fill = randColor())

def randColor() :
    r,g,b = random.randint(0,256), random.randint(0,256), random.randint(0,256)
    return "#%02X%02X%02X" % (r, g, b)
