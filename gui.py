from Tkinter import *

from Tkinter import END, N, S, E, W, Scrollbar, Text


gui = Tk()
gui.title("^_^")
gui.geometry("1070x700")
gui.configure(background='white')

h = Label(gui, text="Wade Hacking Tool", fg="dark green")
w = Label(gui, text="Website", fg="dark green")
e = Label(gui, text="Username", fg="dark green")

h.grid(row=0, column=2)
w.grid(row=3, column=0)
e.grid(row=4, column=0)

w_field = Entry(gui)
e_field = Entry(gui)

w_field.grid(row=3, column=2, ipadx="100")
e_field.grid(row=4, column=2, ipadx="100")

v = IntVar()
Radiobutton(gui, text='Dictionary', variable=v, value=1).grid(row=5, column=1)
Radiobutton(gui, text='Bruteforce', variable=v, value=2).grid(row=6, column=1)

s = Button(gui, text="Attack", fg="Black", bg="white", height=2, width=10)
s.grid(row=8, column=1)



gui.mainloop()

