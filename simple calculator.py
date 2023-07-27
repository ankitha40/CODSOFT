import tkinter as tk
import math

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")


# Create an entry widget to display and input values
e = tk.Entry(root, width=20, borderwidth=4)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button clicks for numbers
def button_clicked(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(tk.END, str(current) + str(number))

# Function to clear the entry field
def button_clear():
    e.delete(0, tk.END)

# Functions to handle different arithmetic operations
def button_addition():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_multiplication():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_division():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_squareroot():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "squareroot"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_round():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "round"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_factorial():
    first_number = e.get()
    global f_num
    global math_operation
    math_operation = "factorial"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_dot():
    current = e.get()
    if '.' not in current:
        e.insert(tk.END, '.')

def button_equal():
    second_num = e.get()
    e.delete(0, tk.END)

    # Perform the selected arithmetic operation based on the math_operation value
    if math_operation == "factorial":
        e.insert(tk.END, math.factorial(f_num))
    elif math_operation == "addition":
        e.insert(tk.END, f_num + int(second_num))
    elif math_operation == "subtraction":
        e.insert(tk.END, f_num - int(second_num))
    elif math_operation == "multiplication":
        e.insert(tk.END, f_num * int(second_num))
    elif math_operation == "division":
        e.insert(tk.END, f_num / int(second_num))
    elif math_operation == "squareroot":
        e.insert(tk.END, round(math.sqrt(f_num), 2))
    elif math_operation == "round":
        e.insert(tk.END, round(f_num))

# Create buttons for numbers, arithmetic operations, and other functions
button_1 = tk.Button(root, text="1", command=lambda: button_clicked(1))
button_2 = tk.Button(root, text="2", command=lambda: button_clicked(2))
button_3 = tk.Button(root, text="3", command=lambda: button_clicked(3))
button_4 = tk.Button(root, text="4", command=lambda: button_clicked(4))
button_5 = tk.Button(root, text="5", command=lambda: button_clicked(5))
button_6 = tk.Button(root, text="6", command=lambda: button_clicked(6))
button_7 = tk.Button(root, text="7", command=lambda: button_clicked(7))
button_8 = tk.Button(root, text="8", command=lambda: button_clicked(8))
button_9 = tk.Button(root, text="9", command=lambda: button_clicked(9))
button_0 = tk.Button(root, text="0", command=lambda: button_clicked(0))
button_c = tk.Button(root, text="C", command=button_clear)
button_squareroot = tk.Button(root, text="√", command=button_squareroot)
button_division = tk.Button(root, text="/", command=button_division)
button_round = tk.Button(root, text="<_", command=button_round)
button_multiply = tk.Button(root, text="*", command=button_multiplication)
button_subtract = tk.Button(root, text="-", command=button_subtract)
button_dotting = tk.Button(root, text=".", command=button_dot)
button_equal = tk.Button(root, text="=", command=button_equal)
button_addition = tk.Button(root, text="+", command=button_addition)
button_factorial = tk.Button(root, text="!", command=button_factorial)

# Position the buttons in the grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_division.grid(row=1, column=3)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)
button_squareroot.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_dotting.grid(row=4, column=2)
button_addition.grid(row=4, column=3)
button_round.grid(row=5, column=0)
button_c.grid(row=5, column=1)
button_factorial.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

# Start the Tkinter main event loop
root.mainloop()
