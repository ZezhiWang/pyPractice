   
from draw import *

    
#___main___
window=Tk()
the_canvas=Canvas(window,width=400,height=400)
the_canvas.grid(row=0,column=0)

# draws a ring centered as given x & y coord
drawRing(the_canvas, 300, 300, 150, 50, randColor())

# draws a square centered as given x & y coord and width
drawDiamond(the_canvas, 300, 300, 100,  "pink")


window.mainloop()
