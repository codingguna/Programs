import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Root Window Only")

lb=tk.Label(root,text='hi')
lb.pack()
# Run the Tkinter event loop
root.mainloop()

