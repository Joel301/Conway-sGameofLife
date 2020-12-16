import tkinter as tk

from math import trunc

def coordinateToSquare(squareNumber,xsize=1200):
    # Create rectangle with coordinates x1,y1,x2,y2
    y1 = trunc(squareNumber/xsize)*10
    x1 = (squareNumber*10)-y1*xsize
    return (x1,y1,x1+10,y1+10)

class form(tk.Frame):

    def __init__(self, master=None, xsize=120, ysize=70):
        super().__init__(master)
        self.xsize = xsize
        self.nSquares = xsize*ysize
        self.master = master

        self.master.geometry("x".join([str(xsize*10), str(ysize*10)]))
        self.master.title('The game of life')
        self.window = tk.Canvas(
            self.master, width=xsize*10, height=ysize*10, bg='grey')
        self.window.pack()
        self.window.create_rectangle(
            0, 590, 10, 600, fill="blue")
        self.window.create_rectangle(
            0, 0, 10, 10, fill="red")
        self.pack()
        self.draw_enviroment()
        self.mainloop()

    def draw_enviroment(self, args=[]):
        if not args:
            for r in range(self.nSquares):
                # Create rectangle with coordinates x1,y1,x2,y2
                self.window.create_rectangle(coordinateToSquare(r,self.xsize))
