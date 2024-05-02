import tkinter as tk

def convert():
    num = int(entry.get())
    celcius = (num - 32) * 5 / 9
    result_lb.config(text=str(num)+" Farenhit = " + str(round(celcius,2)))

window = tk.Tk()
window.title("farenhit to celcius converter")
window.minsize(320,320)

input_lb = tk.Label(window, text="farenhit:")
input_lb.grid(row=0,column=0)

entry = tk.Entry(window)
entry.grid(row=0,column=1)

calculate_bt = tk.Button(window, text="convert", command=convert)
calculate_bt.grid(row=0,column=2)

result_lb = tk.Label(window, text="")
result_lb.grid(row=1,columnspan=2)

window.mainloop()
