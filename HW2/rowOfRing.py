# description: This is to draw a row of rings

# author : WANG, ZEZHI

# date: Sep,11 2015

import random

from Tkinter import *

print "Please input as: rowOfRings(y,n)"

window=Tk()
the_canvas=Canvas(window,width=400,height=400)
the_canvas.grid(row=0,column=0)

def rowOfRings(y,n):
    r = int (200 / n)
    for i in range (0,n):
        drawRing((2*i+1)*r,y,r,random.randint(1,r))
    window.mainloop()


def drawRing(x,y,r,w) :
    p1_x,p1_y = x - r, y - r
    p2_x,p2_y = x + r, y + r
    the_canvas.create_oval(p1_x,p1_y,p2_x,p2_y,fill = randColor()) 
    the_canvas.create_oval(p1_x+w,p1_y+w,p2_x-w,p2_y-w,fill='white')

def randColor() :
    r,g,b = random.randint(0,256), random.randint(0,256), random.randint(0,256)
    return "#%02X%02X%02X" % (r, g, b)
