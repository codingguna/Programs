import tkinter as tk

def factorial():

    number = int(entry.get())

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    result_lb.config(text="Factorial of " + str(number) + " is " + str(factorial))

window = tk.Tk()
window.title("Factorial Calculator")
window.minsize(320,320)

lb = tk.Label(window, text="Enter a number:")
lb.grid(row=0,column=0)

entry = tk.Entry(window)
entry.grid(row=0,column=1)

calculate_bt = tk.Button(window, text="Calculate Factorial", command=factorial)
calculate_bt.grid(row=0,column=2)

result_lb = tk.Label(window, text="")
result_lb.grid(row=1,columnspan=2)

window.mainloop()
