from tkinter import *

def calculate():
  
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    sum = num1 + num2
    result_lb.config(text="Result of Addition: " + str(sum))

window = Tk()
window.title("Simple Calculator")
window.geometry('420x300')

label1 = Label(window, text="Enter First Number:")
label2 = Label(window, text="Enter Second Number:")

entry1 = Entry(window)
entry2 = Entry(window)

calculate_bt = Button(window, text="Calculate", command=calculate)

result_lb = Label(window, text="Result of Addition:")

label1.grid(row=1, column=0)
entry1.grid(row=1, column=1)
label2.grid(row=2, column=0)
entry2.grid(row=2, column=1)
calculate_bt.grid(rowspan=1, column=2)
result_lb.grid(row=3,columnspan=1)

window.mainloop()
