import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    for i in range(101):
     
        time.sleep(0.10)  
        progress['value'] = i
        lb1.configure(text=str(i)+'%')
        lb2.configure(text=str(i//10)+"/10 tasks completed")
        root.update_idletasks()
    progress.stop()

root = tk.Tk()
root.title("tk")
root.geometry('300x200')

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack()


lb1=tk.Label(root,text="0%")
lb1.pack()

lb2=tk.Label(root,text="0/10 tasks completed")
lb2.pack()

start_button = tk.Button(root, text="Download", command=start_progress)
start_button.pack()

root.mainloop()
