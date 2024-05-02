from tkinter import *

# Function to calculate the sum of two numbers
def add():
  # Get the numbers from the entry fields
  num1 = float(entry1.get())
  num2 = float(entry2.get())

  # Calculate the sum
  su = num1 + num2
  print(su)
  # Update the label with the result
  entry3.insert(0,str(su))
def sub():
    n=float(entry1.get())
    m=float(entry2.get())
    s=n-m
    print(s)
    entry3.insert(0,str(s))
# Create the main window
window = Tk()
window.title("Simple Calculator")
window.minsize(300,300)
# Create labels for the entry fields
label1 = Label(window, text="First number")
label2 = Label(window, text="Second number")

# Create entry fields for the numbers
entry1 = Entry(window)
entry2 = Entry(window)
entry3=Entry(window)
# Create a button to trigger the calculation
add_button = Button(window, text="Add", command=add)
sub_bt=Button(window,text="Subract",command=sub)
# Create a label to display the result
result_label = Label(window, text="Result                      ")

# Arrange the widgets on the window
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
add_button.grid(row=2, columnspan=1)
sub_bt.grid(row =2,columnspan=2)
result_label.grid(row=3, column=0)
entry3.grid(row=3,column=1)
# Run the main loop
window.mainloop()
