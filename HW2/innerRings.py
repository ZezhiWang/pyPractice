# description: This is to draw inner rings

# author : WANG, ZEZHI

# date: Sep,11 2015

import random

from Tkinter import *

print "Please input as: innerRings(n) "

window = Tk()
the_canvas = Canvas(window,width = 400, height = 400)
the_canvas.grid(row = 0, column = 0)

def innerRings(n):
    w = int(200 / n)
    for i in range (0, n):
        drawCircles(200,200,w * (n - i))
    window.mainloop()

def drawCircles(x,y,w):
    the_canvas.create_oval(x - w, y - w, x + w, y + w, fill = randColor())

def randColor():
    r,g,b = random.randint(0,256), random.randint(0,256), random.randint(0,256)
    return "#%02x%02x%02x" % (r, g, b)
