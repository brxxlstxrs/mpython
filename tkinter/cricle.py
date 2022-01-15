import tkinter
from random import randint


def draw(event):
    x0 = randint(0, 300)
    y0 = randint(0, 300)
    interval = randint(50, 300)
    x1 = x0 + interval
    y1 = y0 + interval
    canvas.create_oval((x0, y0), (x1, y1), fill='red')  # type: ignore
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
