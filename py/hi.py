from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("calc")

label1=Label(root,text="Enter the fitst number")
label2=Label(root,text="Enter the second number")
label3=Label(root,text="Result:")
entry1=Entry(root)
entry2=Entry(root)
def cal():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a+b
    label3.config(text="result:"+str(c))
button1=Button(root,text="calculate",command=cal)

label1.grid(row=0,column=1)
label2.grid(row=1,column=1)
label3.grid(row=3,column=1)
entry1.grid(row=0,column=2)
entry2.grid(row=1,column=2)
button1.grid(rowspan=1,column=3)
root.mainloop()