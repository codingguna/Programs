from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Define the geometry of window
win.geometry("600x400")

#Create a canvas object
c= Canvas(win,width=400, height=400 ,bg="white")
c.pack()

#Draw an Oval in the canvas
c.create_oval(10,120,210,220,fill="pink")
c.create_line(10,120,210,220,fill="red")
win.mainloop()