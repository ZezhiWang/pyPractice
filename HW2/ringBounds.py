# description: This is to draw a bounded ring

# author : WANG, ZEZHI

# date: Sep,12 2015

from Tkinter import *

print "Please input as: ringInBounds(x,y,radius,width,color)"

window=Tk()

def ringInBounds(x,y,radius,width,color):
    if  x - radius > 0 and x + radius < 400 and y - radius > 0 and y + radius < 400 :
        drawRing(x, y, radius, width, color)
    else :
        print "Error:Ring centered at (%d, %d) with radius %d is out of bounds."%(x,y,radius)

def drawRing(x, y, radius,width, color) :
    the_canvas=Canvas(window,width=400,height=400)
    the_canvas.grid(row=0,column=0)
    the_canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color) 
    the_canvas.create_oval(x - radius + width, y - radius + width, x + radius - width, y + radius - width, fill='white')
    window.mainloop()
