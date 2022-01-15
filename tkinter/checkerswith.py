import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
for i in range(0, 600, 75):
    canvas.create_line((i, 0), (i, 600), fill='black')  # type: ignore
    canvas.create_line((0, i), (600, i), fill='black')  # type: ignore
for y in range(0, 225, 75):
    if y % 2 == 0:
        for x in range(0, 600, 150):
            canvas.create_oval((x, y), (x + 75, y + 75), fill='red')
    else:
        for x in range(75, 600, 150):
            canvas.create_oval((x, y), (x + 75, y + 75), fill='red')

for y in range(375, 600, 75):
    if y % 2 == 0:
        for x in range(0, 600, 150):
            canvas.create_oval((x, y), (x + 75, y + 75), fill='blue')
    else:
        for x in range(75, 600, 150):
            canvas.create_oval((x, y), (x + 75, y + 75), fill='blue')
canvas.pack()
master.mainloop()
