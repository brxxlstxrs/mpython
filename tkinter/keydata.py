import tkinter


def show_key(event):
    kdata = f'{event.keysym=}\n{event.char=}\n'
    kdata += f'{event.keysym_num=}\n{event.keycode=}'
    kdata = kdata.replace('event.', '')
    label.config(text=kdata)


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()
