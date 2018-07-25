# description: This is to draw a ring

# author : WANG, ZEZHI

# date: Sep,12 2015

from draw import *

window=Tk()
the_canvas=Canvas(window,width=400,height=400)
the_canvas.grid(row=0,column=0)

drawRing(the_canvas, 200, 200, 150, 50, "light blue")

window.mainloop()
