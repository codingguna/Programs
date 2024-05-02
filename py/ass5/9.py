from tkinter import *
from tkinter import messagebox

def login():
    email=ent1.get()
    pasw=ent2.get()
    users=["gs400pass",'thamizhi133','senthilsk10','harimb225']
    password=['guna','inba','senthil','hari']
    if email in users and pasw in password :
        messagebox.showinfo("login info","Login Scusses..")
    elif email in users :
        messagebox.showerror("login error",'incorrect password !')
    elif pasw in password:
        messagebox.showerror("lgoin error",'incorrect user_name')
    else:
        messagebox.showerror('login error','entre correct user_name & password')

root=Tk()
root.title("login form")
root.geometry('300x300')

ent1=Entry(root)

ent2=Entry(root)

ulb =Label(root, text="Username:")

plb =Label(root, text="Password:")

bt=Button(root,text="Login",command=login)

ulb.grid(row=0, column=0, padx=10, pady=5)
ent1.grid(row=0, column=1, padx=10, pady=5)
plb.grid(row=1, column=0, padx=10, pady=5)
ent2.grid(row=1, column=1, padx=10, pady=5)
bt.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()