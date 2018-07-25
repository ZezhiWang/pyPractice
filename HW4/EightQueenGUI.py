import EightQueen
from Tkinter import *

def draw_config(canvas,solution_tuple,board_size):
    global canvasSize
    cellsize=canvasSize/board_size
    for j in range(board_size):
        for k in range(board_size):
            if (j+k)%2==0:
                cellcolor='gray'
            else:
                cellcolor='white'
            canvas.create_rectangle(j*cellsize,k*cellsize,(j+1)*cellsize,(k+1)*cellsize,fill=cellcolor)
        if j<len(solution_tuple):
            ell=solution_tuple[j]
            canvas.create_oval(j*cellsize+cellsize/4,ell*cellsize+cellsize/4,(j+1)*cellsize-cellsize/4,(ell+1)*cellsize-cellsize/4,fill='yellow')

def buttonHandler(ev):
    if sizeEntry.get() == '':
        sizeEntry.insert(0,'8')
    size=int(sizeEntry.get())
    if ev.widget==goButton:
        solList = EightQueen.testList(size)
        sol=solList[-1]
        canvas.update_idletasks()
        draw_config(canvas,sol,size)
    elif ev.widget==showButton:
        solList = EightQueen.testList(size)
        print len(solList)
        for sol in solList:
            print "Sol: ", sol
            canvas.update_idletasks()
            canvas.after(1000)
            canvas.delete('all')
            draw_config(canvas,sol,size)
        



w=Tk()
canvasSize=640
canvas=Canvas(w,width=canvasSize,height=canvasSize)
canvas.grid(row=0,column=0,columnspan=3)
goButton=Button(w,text='Go')
goButton.grid(row=1,column=0)
goButton.bind('<Button-1>',buttonHandler)
sizeEntry=Entry(w,width=10)
sizeEntry.grid(row=1,column=1)
showButton=Button(w,text='Show Steps')
showButton.grid(row=1,column=2)
showButton.bind('<Button-1>',buttonHandler)
w.mainloop()
