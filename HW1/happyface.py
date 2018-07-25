# description: This is my first program 

# author : WANG, ZEZHI

# date: August 31, 2015

from Tkinter import *
window=Tk()
the_canvas=Canvas(window,width=500,height=500)
the_canvas.grid(row=0,column=0)
# These next four statements are the ones you should play with for your
# program. LEAVE EVERYTHING ELSE (apart from the comments) ALONE
the_canvas.create_oval(100,100,400,400,fill='green') # draws the face 
the_canvas.create_arc(100,325,400,200,start=215,extent=110,style=ARC) # draws the mouth 
the_canvas.create_oval(180,225,222,187,fill='red') # draws the left eye
the_canvas.create_oval(278,225,320,187,fill='blue') # draws the right eye 
window.mainloop()
