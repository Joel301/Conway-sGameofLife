import tkinter as tk
import time
from form import form
from arrays import arrays

XSIZE = 5
YSIZE = 5

app = form(master=tk.Tk(), xsize=XSIZE, ysize=YSIZE)

ar = arrays(XSIZE,YSIZE)
ar.now.loc[1:3, 2] = 1
app.draw_enviroment()
while True:
    time.sleep(.01)
    ar.do_tick()
    app.update_enviroment(ar.now)

