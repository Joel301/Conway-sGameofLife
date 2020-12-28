import tkinter as tk
import pandas as pd
from math import trunc



def coordinateToSquare(squareNumber, xsize=1200):
    # Create rectangle with coordinates x1,y1,x2,y2
    y1 = trunc(squareNumber/xsize)*10
    x1 = (squareNumber*10)-y1*xsize
    return (x1, y1, x1+10, y1+10)

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
        self.pack()
        self.draw_enviroment()
        # self.master.update_idletasks()

    def update_enviroment(self,arr):
        for cell in range(self.nSquares):
            y = trunc(cell/self.xsize)
            x = cell - y*self.xsize
            if arr.loc[y][x]:
                self.window.itemconfig(
                    self.arraySquares[cell],
                    fill='white'
                )
            else:
                self.window.itemconfig(
                        self.arraySquares[cell],
                        fill='grey'
                    )
        self.window.update()

    def draw_enviroment(self):
        self.arraySquares = []
        for r in range(self.nSquares):
            # Create rectangle with coordinates x1,y1,x2,y2
            self.arraySquares.append(self.window.create_rectangle(
                coordinateToSquare(r, self.xsize)))
        self.master.update()

    def coordinatesToNumber(self, x,y):
        return (self.xsize*y)+x