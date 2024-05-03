from tkinter import *

def add():
  num1 = float(entry1.get())
  num2 = float(entry2.get())

  # Calculate the sum
  su = num1 + num2
  print(su)
  entry3.delete(0,END)
  entry3.insert(0,str(su))
def sub():
    n=float(entry1.get())
    m=float(entry2.get())
    s=n-m
    print(s)
    entry3.delete(0,END)
    entry3.insert(0,str(s))

window = Tk()
window.title("Simple Calculator")
window.geometry('300x300')

label1 = Label(window, text="First number")
label2 = Label(window, text="Second number")

entry1 = Entry(window)
entry2 = Entry(window)
entry3=Entry(window)

add_button = Button(window, text="Add", command=add)
sub_bt=Button(window,text="Subract",command=sub)

result_label = Label(window, text="Result                      ")

label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
add_button.grid(row=2, columnspan=1)
sub_bt.grid(row =2,columnspan=2)
result_label.grid(row=3, column=0)
entry3.grid(row=3,column=1)

window.mainloop()
