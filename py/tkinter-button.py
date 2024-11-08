from tkinter import *

root = Tk()

root.title("Welcome to GeekForGeeks")

root.geometry('350x200')

lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

def clicked():
	lbl.configure(text = "I just got clicked")

btn = Button(root, text = "Click me" ,fg = "red", command=clicked)
btn.grid(column=1, row=0)

roo = Tk()

roo.title("Welcome to GeekForGeeks")

roo.geometry('350x200')

lbl = Label(roo, text = "Are you a Geek?")
lbl.grid()

txt = Entry(roo, width=10)
txt.grid(column =1, row =0)

def clicked():

	res = "You wrote" + txt.get()
	lbl.configure(text = res)

btn = Button(roo, text = "Click me" ,
			fg = "red", command=clicked)

btn.grid(column=2, row=0)

ro = Tk()

ro.title("Welcome to GeekForGeeks")

ro.geometry('350x200')

menu = Menu(ro)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
ro.config(menu=menu)

lbl = Label(ro, text = "Are you a Geek?")
lbl.grid()

txt = Entry(ro, width=10)
txt.grid(column =1, row =0)

def clicked():

	res = "You wrote" + txt.get()
	lbl.configure(text = res)

btn = Button(ro, text = "Click me" ,fg = "red", command=clicked)

btn.grid(column=2, row=0)

ro.mainloop()
roo.mainloop()
root.mainloop()