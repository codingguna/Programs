import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("hello python ")
window.geometry("400x400")

ckbt=tk.Checkbutton(window,text="Cricket")
ckbt.grid(row=2,column=1)

ckbt1=tk.Checkbutton(window,text="Tennis")
ckbt1.grid(row=2,column=3)

rb=tk.Radiobutton(window,text="male")
rb.grid(row=1,column=1)

rb1=tk.Radiobutton(window,text='female')
rb1.grid(row=1,column=3)

lb=tk.Listbox(window)
lb.insert(1, 'One')
lb.insert(2,'Two')
lb.insert(3,'Three')
lb.insert(4,'Four')
lb.grid(row=3,column=6)

cb=ttk.Combobox(window,values=['One','Two','Three','Four'])
cb.grid(row=3,column=2)


window.mainloop()