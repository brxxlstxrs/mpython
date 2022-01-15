import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
for i in range(0, 600, 75):
    canvas.create_line((i, 0), (i, 600), fill='black')  # type: ignore
    canvas.create_line((0, i), (600, i), fill='black')  # type: ignore
canvas.pack()
master.mainloop()
