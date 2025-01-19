# This is a version with a gui.
#  Based off of one of my other calculators, but ai made the GUI because i suck at that.
#  But i wrote the code that it is based on.


# filepath: /C:/Users/dylan/Python Calculator w gui.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def divide():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
        else:
            result = float(entry1.get()) / float(entry2.get())
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Use ttk for modern themed widgets
style = ttk.Style(root)
style.theme_use('clam')  # You can try 'clam', 'alt', 'default', 'classic'

# Create and place the widgets
ttk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = ttk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = ttk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

ttk.Button(root, text="Add", command=add).grid(row=2, column=0, padx=10, pady=10)
ttk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1, padx=10, pady=10)
ttk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0, padx=10, pady=10)
ttk.Button(root, text="Divide", command=divide).grid(row=3, column=1, padx=10, pady=10)

result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
    
